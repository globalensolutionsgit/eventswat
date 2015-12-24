from events.models import *
from postevent.models import Postevent

def globalactivity(request):
	eventscategory =  EventsCategory.objects.all()
	eventssubcategory=EventsSubCategory.objects.all()
	recentad = Postevent.objects.filter(admin_status='true').order_by('-id')[:4]
	path = request.path
	return {'eventssubcategory':eventssubcategory,'eventscategory':eventscategory,'recentad':recentad,'path':path}
