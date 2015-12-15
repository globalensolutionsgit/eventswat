# coding: utf-8 
# -*- coding: utf-8 -*-

import re
from django.middleware import csrf
from django.db.models import Q

from actors import globals, actor_ip
from core import helper
from control.models import RecentlyviewLeads, RecentlySearch
from fixido.util import ip_checking

headers = ('HTTP_CLIENT_IP', 'HTTP_X_FORWARDED_FOR', 'HTTP_X_FORWARDED',
    'HTTP_X_CLUSTERED_CLIENT_IP', 'HTTP_FORWARDED_FOR', 'HTTP_FORWARDED',
    'REMOTE_ADDR')

# Back ported from Django trunk
# This code was mostly based on ipaddr-py
# Copyright 2007 Google Inc. http://code.google.com/p/ipaddr-py/
# Licensed under the Apache License, Version 2.0 (the "License").
ipv4_re = re.compile(r'^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$')

def is_valid_ipv4_address(ip_str):
    return bool(ipv4_re.match(ip_str))


def is_valid_ipv6_address(ip_str):
    """
    Ensure we have a valid IPv6 address.

    Args:
        ip_str: A string, the IPv6 address.

    Returns:
        A boolean, True if this is a valid IPv6 address.

    """
    # We need to have at least one ':'.
    if ':' not in ip_str:
        return False

    # We can only have one '::' shortener.
    if ip_str.count('::') > 1:
        return False

    # '::' should be encompassed by start, digits or end.
    if ':::' in ip_str:
        return False

    # A single colon can neither start nor end an address.
    if ((ip_str.startswith(':') and not ip_str.startswith('::')) or
            (ip_str.endswith(':') and not ip_str.endswith('::'))):
        return False

    # We can never have more than 7 ':' (1::2:3:4:5:6:7:8 is invalid)
    if ip_str.count(':') > 7:
        return False

    # If we have no concatenation, we need to have 8 fields with 7 ':'.
    if '::' not in ip_str and ip_str.count(':') != 7:
        # We might have an IPv4 mapped address.
        if ip_str.count('.') != 3:
            return False

    ip_str = _explode_shorthand_ip_string(ip_str)

    # Now that we have that all squared away, let's check that each of the
    # hextets are between 0x0 and 0xFFFF.
    for hextet in ip_str.split(':'):
        if hextet.count('.') == 3:
            # If we have an IPv4 mapped address, the IPv4 portion has to
            # be at the end of the IPv6 portion.
            if not ip_str.split(':')[-1] == hextet:
                return False
            if not is_valid_ipv4_address(hextet):
                return False
        else:
            try:
                # a value error here means that we got a bad hextet,
                # something like 0xzzzz
                if int(hextet, 16) < 0x0 or int(hextet, 16) > 0xFFFF:
                    return False
            except ValueError:
                return False
    return True

def _sanitize_ipv4_mapping(ip_str):
    """
    Sanitize IPv4 mapping in a expanded IPv6 address.

    This converts ::ffff:0a0a:0a0a to ::ffff:10.10.10.10.
    If there is nothing to sanitize, returns an unchanged
    string.

    Args:
        ip_str: A string, the expanded IPv6 address.

    Returns:
        The sanitized output string, if applicable.
    """
    if not ip_str.lower().startswith('0000:0000:0000:0000:0000:ffff:'):
        # not an ipv4 mapping
        return ip_str

    hextets = ip_str.split(':')

    if '.' in hextets[-1]:
        # already sanitized
        return ip_str

    ipv4_address = "%d.%d.%d.%d" % (
        int(hextets[6][0:2], 16),
        int(hextets[6][2:4], 16),
        int(hextets[7][0:2], 16),
        int(hextets[7][2:4], 16),
    )

    result = ':'.join(hextets[0:6])
    result += ':' + ipv4_address

    return result

def _unpack_ipv4(ip_str):
    """
    Unpack an IPv4 address that was mapped in a compressed IPv6 address.

    This converts 0000:0000:0000:0000:0000:ffff:10.10.10.10 to 10.10.10.10.
    If there is nothing to sanitize, returns None.

    Args:
        ip_str: A string, the expanded IPv6 address.

    Returns:
        The unpacked IPv4 address, or None if there was nothing to unpack.
    """
    if not ip_str.lower().startswith('0000:0000:0000:0000:0000:ffff:'):
        return None

    hextets = ip_str.split(':')
    return hextets[-1]

def _explode_shorthand_ip_string(ip_str):
    """
    Expand a shortened IPv6 address.

    Args:
        ip_str: A string, the IPv6 address.

    Returns:
        A string, the expanded IPv6 address.

    """
    if not _is_shorthand_ip(ip_str):
        # We've already got a longhand ip_str.
        return ip_str

    new_ip = []
    hextet = ip_str.split('::')

    # If there is a ::, we need to expand it with zeroes
    # to get to 8 hextets - unless there is a dot in the last hextet,
    # meaning we're doing v4-mapping
    if '.' in ip_str.split(':')[-1]:
        fill_to = 7
    else:
        fill_to = 8

    if len(hextet) > 1:
        sep = len(hextet[0].split(':')) + len(hextet[1].split(':'))
        new_ip = hextet[0].split(':')

        for _ in xrange(fill_to - sep):
            new_ip.append('0000')
        new_ip += hextet[1].split(':')

    else:
        new_ip = ip_str.split(':')

    # Now need to make sure every hextet is 4 lower case characters.
    # If a hextet is < 4 characters, we've got missing leading 0's.
    ret_ip = []
    for hextet in new_ip:
        ret_ip.append(('0' * (4 - len(hextet)) + hextet).lower())
    return ':'.join(ret_ip)


def _is_shorthand_ip(ip_str):
    """Determine if the address is shortened.

    Args:
        ip_str: A string, the IPv6 address.

    Returns:
        A boolean, True if the address is shortened.

    """
    if ip_str.count('::') == 1:
        return True
    if filter(lambda x: len(x) < 4, ip_str.split(':')):
        return True
    return False

def get_ip_address(request):
    for header in headers:
        if request.META.get(header, None):
            ip = request.META[header].split(',')[0]
            if ':' in ip and is_valid_ipv6_address(ip) or is_valid_ipv4_address(ip):
                return ip

def update_recently_view_lead(lead, request, method):
    """ Stores recently viewed leads information
        with system id and user id
    """
    system_id = request.COOKIES.get('csrftoken', csrf.get_token(request))
    ip_number = actor_ip()
    
    if request.user.is_authenticated():
        user = request.user.actor
    else:
        user = None
    
    if lead:
        lead.viewed()
        try:
            #leadviewed = RecentlyviewLeads.objects.filter(lead=lead)
            #if leadviewed:
                #leadviewed = leadviewed.filter(
                #    Q(user_id=user) | Q(system_id=system_id))
                #if leadviewed:
                    if not ip_checking(ip_number):
                        # leadviewed = leadviewed[0]
                        # leadviewed.user_id = user
                        # leadviewed.system_id = system_id
                        # leadviewed.method = method
                        # leadviewed.modified = helper.get_now()
                        # leadviewed.ip_number = ip_number
                        # leadviewed.save()
                        leadviewed = RecentlyviewLeads.objects.create(
                            lead=lead, system_id=system_id,
                            user=user, method=method, ip_number=ip_number,
                            modified=helper.get_now()
                        )
                #else:
                #    raise
            #else:
            #    raise
        except Exception, e:
            if not ip_checking(ip_number):
                leadviewed = RecentlyviewLeads.objects.create(
                lead=lead, system_id=system_id,
                user=user, method=method, ip_number=ip_number,
                modified=helper.get_now()            
            )


def update_recent_search(search, request, method):
    """ Stores recently search information
        with system id and user id
    """
    if request.user.is_authenticated():
        user = request.user.actor
    else:
        user = None
    
    system_id = request.COOKIES.get('csrftoken', csrf.get_token(request))
    ip_number = globals.ip
    if search:
        # lead.viewed += 1
        # lead.save()
        if u'�' in search:
            query_string = request.META.get('QUERY_STRING', '').split('&')
            qsl = [qs for qs in query_string if qs.startswith('q=')]
            search = qsl[0].replace('q=', '').decode('latin1') if qsl else u''
        
        if not user:
            rs = RecentlySearch.objects.filter(
                    activity_view=search, system_id=system_id,
                )
        else:
            rs = RecentlySearch.objects.filter(
                    activity_view=search, user=user,
                )
        if rs.count() > 1:
            rs = rs.order_by('-modified')
            rs = rs.exclude(id=rs[0].id)
            rs.delete()
        
        try:
            leadsearch = RecentlySearch.objects.filter(activity_view=search)
            if leadsearch:
                leadsearch = leadsearch.filter(
                    Q(user=user) | Q(system_id=system_id))
                if leadsearch:
                    leadsearch = leadsearch[0]
                    leadsearch.user_id = user
                    leadsearch.system_id = system_id
                    leadsearch.method = method
                    leadsearch.modified = helper.get_now()
                    leadsearch.ip_number = ip_number
                    leadsearch.save()
                else:
                    raise
            else:
                raise
        except Exception, e:
            RecentlySearch.objects.get_or_create(
                activity_view=search, system_id=system_id, user=user,
                method=method, ip_number=ip_number, modified=helper.get_now()
            )

