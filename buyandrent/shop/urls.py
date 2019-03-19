from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('<slug:category_slug>/', views.house_list, 
         name='house_list_by_category'),
    path('<int:id>/<slug:slug>/', views.house_detail,
         name='house_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)