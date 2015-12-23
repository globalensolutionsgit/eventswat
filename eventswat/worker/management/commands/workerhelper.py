from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

class Command(BaseCommand):
  help = "Util functions for worker"

  option_list = BaseCommand.option_list + (
      make_option('--init', action='store_true', dest='init', 
        default=False,help='Init worker settings'),
      make_option('--cleartasks', dest='cleartasks', help='Clear tasks of given lead id and create new one'),
    )


  def handle(self, *args, **options):
    # if options['init']:
    #   self.initworker()
    pass


  def initworker(self):
    from ...models import Worker

    workers = Worker(id='banner_notice_email')
    worker.name = 'Banner Notice Email'
    worker.cls_path = 'worker.workers.EmailNotification_ExpiredAds'
    worker.save()

    workers = Worker(id='user_intrest_notice_email')
    worker.name = 'User Intrest Notice Email'
    worker.cls_path = 'worker.workers.EmailNotification_intrestAds'
    worker.save()