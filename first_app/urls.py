#from django.conf.urls import url
from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path("contact/",views.contact,name='contact'),
    path("about/",views.about,name='about'),
    # path('form1/',views.form1,name='form1'),
    path('form/',views.form,name='form'),
]
