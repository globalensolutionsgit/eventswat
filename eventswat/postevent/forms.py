from django.forms import ModelForm
from postevent.models import Postevent, SubCategoryRelatedFieldValue, Organizer


class PosteventForm(ModelForm):
     class Meta:
         model = Postevent
         fields = '__all__'


class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategoryRelatedFieldValue
        fields = '__all__'


class OrganizerForm(ModelForm):
    class Meta:
        model = Organizer
        fields = '__all__'
