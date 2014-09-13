
import manage_webentries

import PyRSS2Gen.PyRSS2Gen as rss_gen

from django.http import HttpResponse

import time

def strShortDateToRFC822Friendly(strShortDate):
  "Expect the form: 2010-02-30"
  short_time = time.strptime(strShortDate, '%Y-%m-%d')
  time_RFC822 = time.strftime("%a, %d %b %Y %H:%M:%S EST", short_time)
  return time_RFC822

def get_webdoc_as_rss(request):
  web_entries = manage_webentries.getWebEntries()
  base_url = 'http://www.grokit.ca'
  
  items = []
  for web_entry in web_entries:
    rss_item = rss_gen.RSSItem( \
      title = web_entry.getTitle(), \
      description =  web_entry.getBriefDescription(), \
      pubDate = strShortDateToRFC822Friendly(web_entry.getDate()), \
      guid = base_url + '/cnt/' + web_entry.getEntrySubUrl() )
    items.append(rss_item)
  
  rss_obj = rss_gen.RSS2( title = 'David Webdoc Full List', link=base_url, description = 'Webdoc, all by date', items = items )
  
  return( HttpResponse( rss_obj.to_xml(), content_type = "application/rss+xml" ) )
  
