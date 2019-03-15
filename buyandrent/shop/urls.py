from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'shop'
urlpatterns = [
    url(r'^$', views.house_list, name='house_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.house_list,
        name='house_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.house_detail,
        name='house_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)