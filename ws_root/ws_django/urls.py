from django.conf.urls import *

import settings

urlpatterns = patterns('',
  (r'^cnt/([^/]+)/$', 'ws_django.webdoc.views.index'),
  (r'^tag/([^/]+)/$', 'ws_django.webdoc.views.tags'),
  (r'^cnt/([^/]+)/comment/$', 'ws_django.webdoc.views.incoming_comment'),
  (r'^data_entry$', 'ws_django.incoming_data.views.process_incoming_data'),
  (r'^data_entry/read$', 'ws_django.incoming_data.views.get_all_messages'),
  (r'^cnt/$', 'ws_django.webdoc.views.index'),
  (r'^canvas_fun/$', 'ws_django.canvas_fun.views.index'),
  (r'^testapp/$', 'ws_django.testapp.views.index'),
  (r'^testapp/comment/$', 'ws_django.testapp.views.incoming_comment'),
  (r'^testapp/redirectafterpost/$', 'ws_django.testapp.views.redirectafterpost'),
  (r'^debug/$', 'ws_django.debug.views.index'),
  (r'^spc/webdoc_rss$', 'ws_django.webdoc.rss.get_webdoc_as_rss'),
  (r'^spc/lafontaine/([^/]+)/$', 'ws_django.spc.lafontaine.views.index'),
  (r'^spc/lai/(.*)', 'ws_django.spc.lai-bisukasu.views.index'),
  (r'^spc/gettest/(.*)', 'ws_django.spc.gettest.views.index'),
  (r'^spc/fractals/in/$', 'ws_django.spc.fractal_canvas.views.store_fractal'),
  (r'^spc/fractals/(.*)$', 'ws_django.spc.fractal_canvas.views.index'),
  (r'^spc/atoms/(.*)$', 'ws_django.spc.atoms.views.index'),
  (r'^spc/timer/(.*)', 'ws_django.spc.timers.views.index'),
  (r'^spc/computer_science_review/(.*)', 'ws_django.spc.computer_science_review.views.index'),
  (r'^spc/phones/([^/]+)/$', 'ws_django.spc.phones.views.index'),
  #(r'^debug/dump_dbs/$', 'ws_django.debug.views.dump_dbs'),
  (r'^contact', 'ws_django.contact.views.index'),
  (r'^$', 'ws_django.webdoc.views.index'),
  #(r'(.*)', 'ws_django.notfound.views.index')
)

# Mirror what would happen with google app engine on local mode
if settings.DEBUG:
  urlpatterns += patterns('',
      (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '../static'}),
  )

