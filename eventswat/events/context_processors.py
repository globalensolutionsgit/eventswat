from events.models import *
from postevent.models import Postevent, PosteventPoster
from usermanagement.forms import UserCreationForm, UserLoginForm

def globalactivity(request):
	eventscategory =  EventsCategory.objects.all()
	eventssubcategory=EventsSubCategory.objects.all()	
	recent_poster = PosteventPoster.objects.all().order_by('-id')[:6]	
	path = request.path
	city = City.objects.all()
	registeration_form = UserCreationForm()
	login_form = UserLoginForm()
	return {'eventssubcategory':eventssubcategory,'eventscategory':eventscategory, 'recent_poster':recent_poster, 'path':path,'city':city, 'registeration_form':registeration_form, 'login_form':login_form}
