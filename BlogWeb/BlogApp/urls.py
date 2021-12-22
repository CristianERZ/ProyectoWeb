from django.urls import path

from BlogApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', views.home, name="Home"),
    path('info/', views.info, name="Informacion"),
    path('blog/', views.blog, name="Blog"),
    path('contac/', views.contac, name="Contacto"),
   
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
