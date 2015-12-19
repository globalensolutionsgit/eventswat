from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from postevent.models import Postevent, SubCategoryRelatedFieldValue, Organizer


class HorizRadioRenderer(forms.RadioSelect.renderer):
    """
    this overrides widget method to put radio buttons horizontally
    instead of vertically.
    http://stackoverflow.com/questions/16773579/customize-radio-buttons-in-django
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class PosteventForm(forms.ModelForm):

    class Meta:
        model = Postevent
        fields = ['event_type', 'event_category', 'event_subcategory',
                  'event_title','event_description', 'event_startdate_time',
                   'event_enddate_time', 'event_poster', 'terms_and_condition',
                   'event_website', 'is_webinar', 'venue', 'city', 'state',
        ]
        widgets = {
            'event_type': forms.RadioSelect(renderer=HorizRadioRenderer),
        }
        error_messages = {
            'event_title': {
                'max_length': _("This writer's name is too long."),
            },
        }

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = '__all__'
