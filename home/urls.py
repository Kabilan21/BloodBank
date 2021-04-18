from django.urls import path , include
from .import views
urlpatterns = [
    path('', views.bloodshare ,name='bloodshare'),
    path('register',views.register,name ='blood_register' ),
    path('search',views.bloodsearch,name='blood_search'),
    path('profile',views.bloodprofile,name='bloodprofile'),
    path('profile/update',views.profileupdate , name = 'profileupdate'),
    path('need',views.bloodneed , name ='bloodneed')
]