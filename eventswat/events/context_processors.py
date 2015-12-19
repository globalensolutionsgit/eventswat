from events.models import *
from postevent.models import Postevent

def globalactivity(request):
    eventssubcategory=EventsSubCategory.objects.all()
    recentad = Postevent.objects.filter(admin_status='true').order_by('-id')[:4]
    path = request.path
    return {'eventssubcategory':eventssubcategory,'recentad':recentad,'path':path}
