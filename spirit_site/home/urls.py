from django.conf.urls import url
from home import views

app_name = 'home'

urlpatterns = [
    #url(r'^$',views.spirit,name ='spirit'),
    #url(r'^organizingteam/$',views.organizingteam,name='organizingteam'),
    #url(r'^gallery/$',views.gallery,name='gallery'),
    url(r'^athletics/$',views.athletics,name='athletics'),
    url(r'^badminton/$',views.badminton,name='badminton'),
    url(r'^basketball/$',views.basketball,name='basketball'),
    url(r'^cricket/$',views.cricket,name='cricket'),
    url(r'^lawntennis/$',views.lawntennis,name='lawntennis'),
    url(r'^hockey/$',views.hockey,name='hockey'),
    url(r'^tabletennis/$',views.tabletennis,name='tabletennis'),
    url(r'^football/$',views.football,name='football'),
    url(r'^volleyball/$',views.volleyball,name='volleyball'),
    url(r'^chess/$',views.chess,name='chess')

]
