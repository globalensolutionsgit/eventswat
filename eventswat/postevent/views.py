from events.models import EventsSubCategory
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from events.extra import JSONResponse

@csrf_exempt
def admin_subcategory(request):
    """This function definition for admin postevent add page.Using dependent select boxes.SUbcategory load based on category"""
    if request.is_ajax():
        events = EventsSubCategory.objects.filter(category__id=request.GET.get('id'))
        return JSONResponse([{'name': obj.subcategory_name, 'id': obj.id,} for obj in events])
