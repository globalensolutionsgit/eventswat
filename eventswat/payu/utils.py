from hashlib import sha512
from django.conf import settings


KEYS = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
        'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
        'udf9',  'udf10')


def generate_hash(data):
    """This function make hash key as requirement of payu documentation"""
    keys = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
            'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
            'udf9',  'udf10')
    hash = sha512('')
    for key in KEYS:
        hash.update("%s%s" % (str(data.get(key, '')), '|'))
    hash.update(settings.PAYU_INFO.get('merchant_salt'))
    print "sdfsdfsdfsdfasdfdf", hash.hexdigest().lower()
    return hash.hexdigest().lower()


def verify_hash(data, SALT):
    """This function varify our maked hash correct or not"""
    keys.reverse()
    hash = sha512(settings.PAYU_INFO.get('merchant_salt'))
    hash.update("%s%s" % ('|', str(data.get('status', ''))))
    for key in KEYS:
        hash.update("%s%s" % ('|', str(data.get(key, ''))))
    return (hash.hexdigest().lower() == data.get('hash'))
