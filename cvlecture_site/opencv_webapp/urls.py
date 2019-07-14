from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns =[
    url(r'^$', views.first_view, name='first_view'),
    url(r'^uimage/', views.uimage, name='uimage'),
]
#any input- go to 'first_view' hamsoo
# uimage address input ,go to uimage

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#image upload