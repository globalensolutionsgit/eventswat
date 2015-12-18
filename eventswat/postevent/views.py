from events.models import EventsSubCategory
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from events.extra import JSONResponse
from postevent.forms import PosteventForm,SubCategoryForm,OrganizerForm
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

@csrf_exempt
def admin_subcategory(request):
    """This function definition for admin postevent add page.Using dependent select boxes.SUbcategory load based on category"""
    if request.is_ajax():
        events = EventsSubCategory.objects.filter(category__id=request.GET.get('id'))
        return JSONResponse([{'name': obj.subcategory_name, 'id': obj.id,} for obj in events])

def test(request):
    context = {
    'postevent_form': PosteventForm(),
    'subcategory_form': SubCategoryForm(),
    'organizer_form': OrganizerForm()
    }
    return render_to_response("test.html",context, context_instance=RequestContext(request))
