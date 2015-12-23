from django.contrib import admin
from django import forms
from usermanagement.models import Userprofile


class UserprofileAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'mobile', 'verification_code', 'gender',
              'date_of_birth', 'user_address', 'user_interest', 'profile_pic',
              'is_emailverified', 'twitter_url', 'facebook_url', 'user_type']

    list_display = ('id', 'username', 'email', 'mobile', 'verification_code',
                    'gender', 'date_of_birth', 'user_address', 'profile_pic',
                    'is_emailverified', 'twitter_url', 'facebook_url',
                    'user_type')

    list_filter = ['date_of_birth']
    search_fields = ['id', 'mobile', 'username']
    list_per_page = 50


admin.site.register(Userprofile, UserprofileAdmin)
