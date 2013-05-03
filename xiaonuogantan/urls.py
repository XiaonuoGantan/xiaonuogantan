from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from xiaonuogantan.models import Comment, Post
admin.site.register(Comment)
admin.site.register(Post)

from tastypie.api import Api
from xiaonuogantan.api import PostResource

v1_api = Api(api_name='v1')
v1_api.register(PostResource())

urlpatterns = patterns('',
    url(r"^account/", include("account.urls")),
    # Hook up the tastypie resources
    url(r'^api/', include(v1_api.urls)),

    # Hook up the admin app
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
