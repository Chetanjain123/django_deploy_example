from django.urls import path
from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
app_name= 'basic_app'

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name="other"),

    # path('',views.index,name='index'),
    # path(r'^relative/$',views.relative,name='relative'),
    # path(r'^other/$',views.other,name="other"),
    # #path(r'^base/$',views.base,name="base")

]
