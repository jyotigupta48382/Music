from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url



urlpatterns =[
    url(r'admin/', admin.site.urls),
    url(r"^music/",include('music.urls')),

]
