
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
# from first_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('first_app.urls')),
    # path('index/',views.index,name='index'), 
    # path('',views.index,name='index'), 
    # path("contact/",views.contact,name='contact'),
    # path("about/",views.about,name='about'),
]
