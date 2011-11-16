from django.http import HttpResponse
from dateutil.parser import parse
from google.appengine.api.labs import taskqueue
from datetime import datetime, date, timedelta
from pytz.gae import pytz
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import logging, traceback
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.api import urlfetch


import gdata.calendar

from vobject.icalendar import stringToDate, stringToDateTime

# DeadlineExceededError can live in two different places 
try: 
  # When deployed 
  from google.appengine.runtime import DeadlineExceededError 
except ImportError: 
  # In the development server 
  from google.appengine.runtime.apiproxy_errors import DeadlineExceededError


utc=pytz.timezone('UTC')



def process_gdata(source):
	from events.models import Event
	try:
		gdata_source=source.content
		feed=gdata.calendar.CalendarEventFeedFromString(gdata_source)
		cal_count=0
		for gevent in feed.entry:
			Event.from_gdata(gevent, source)
    
    
	except urlfetch.DownloadError:
		raise
        
	except Exception,e:
                logging.error(traceback.format_exc())
    
    


def fetch_icals(request):
    from models import ICalendarSource
    try:
        if request.method == 'POST':
            cursor=request.POST.get('cursor')
            started=request.POST.get('started')
            parsed_started=parse(started)
            q=ICalendarSource.all().filter('status = ', 'approved').filter('last_fetch < ', parsed_started- relativedelta(hours=+3))
            if cursor:
                q=q.with_cursor(cursor)
            cals= q.fetch(100)
            if cals: 
                params={'cursor': q.cursor(),
                        'started': started}
                taskqueue.add(url='/sources/fetch/', params=params,)
            for ical in cals:
                try:
                    ical.fetch(started)
                except:
                    logging.warning("failed fetching %s" % ical.ical_href)
                    raise
                
    except Exception,e:
                logging.error("%s in \n%s"% (traceback.format_exc(),str(request.POST)))
    return HttpResponse("OK")
     
    
        
def process_ical(source):
	from events.models import Event
	try:
		ical=source.content
		first_vevent_start=ical.find('BEGIN:VEVENT')
		cal_meta=ical[0:first_vevent_start]

		def next_vevent(start):
			end=ical.find('END:VEVENT',start)
			if end > -1:
				end=end+10
				cal=cal_meta+ical[start:end]+"\nEND:VCALENDAR"
				return (cal, end)
			else:
				return(None, None)
		vevent, index=next_vevent(first_vevent_start)   
		while vevent:
			event=Event.from_vcal(vevent, source)
			vevent, index=next_vevent(index)
			

																
	except DeadlineExceededError:
			   return HttpResponse("Deadline Exceeded!")
	except Exception,e:
	   logging.error(traceback.format_exc())
	return HttpResponse("OK")