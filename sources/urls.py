from django.conf.urls.defaults import *
from views import add_source, sources, manage_sources, save_ical, start_fetch_icals, opml, json
from tasks import fetch_icals, split_ical, split_gdata , fetch_icals_test


urlpatterns = patterns('events',
      url(r'^$', sources, name="sources-index"),
      url(r'^opml/$', opml, name="opml"),
      url(r'^json/$', json, name="json"),
      url(r'^manage/$', manage_sources, name="manage-sources"),
      url(r'^add/$', add_source, name="add-source"),
      url(r'^save/$', save_ical, name="save-ical"),
      url(r'^fetch/$', fetch_icals, name="fetch-icals-task"),
      url(r'^split_gdata/$', split_gdata ),
      url(r'^split_ical/$', split_ical, name="split_ical"),
      url(r'^start_fetch_icals/$',start_fetch_icals ),
      url(r'^fetch_icals/$', fetch_icals_test, name="fetch-icals-task-test")

)
