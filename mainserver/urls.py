from django.conf.urls import include, url
from django.contrib import admin
from users.views import login_user
from panel import views as panelviews
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    # Examples:
    #url(r'^$', 'panel.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^', include(admin.site.urls)),
    url(r'^users/', include('users.urls')),
    url(r'^maps/', include('map.urls')),
    url(r'^messages/', include('message.urls')),
    url(r'^speakers/', include('speaker.urls')),
    url(r'^$', panelviews.index, name='index'),
    url(r'^hardwares', panelviews.hardware),
    url(r'^addhardware', panelviews.add_hardware),
    url(r'^addmessage', panelviews.add_message),
    url(r'^maplist$', panelviews.map_list),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]