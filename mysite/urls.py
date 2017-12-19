from django.conf.urls import url,include
from django.contrib import admin
from accounts.views import (login_view,logout_view,register_view)
from home.views import home_view,view_event,create_event
urlpatterns = [
	#url(r'^tech/register/',include('register.urls')),#works
	#url(r'^tech/login/',include('login.urls')),#works
    url(r'^admin/', admin.site.urls),
    url(r'drizzlelore/frontpage/',include('frontpage.urls')),
    url(r'drizzlelore/login/',login_view,name="login"),
    url(r'drizzlelore/logout/',logout_view,name="logout"),
    url(r'drizzlelore/register/',register_view,name="register"),
    url(r'drizzlelore/viewevents',view_event,name="viewevents"),
    url(r'drizzlelore/createEvents',create_event,name="createEvents"),
    url(r'^',home_view,name="home"),
]
