from django.urls import path
from univeristy.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home),
    path('addpage/',addpage,name='add_page'),
    path('page/<str:page_name>/',page,name='language'),
    path('all/',all,name='all')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
