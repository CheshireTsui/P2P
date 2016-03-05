from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'P2P_Project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'P2P_Project.views.home', name='home'),
    url(r'upload/', 'upload_Page.views.upload', name='upload'),
    url(r'show/', 'show_Page.views.show', name='show'),
    url(r"^media/(?P<path>.*)$", \
        "django.views.static.serve", \
        {"document_root": settings.MEDIA_ROOT,}),
)
