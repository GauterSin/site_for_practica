from django.urls import path
from . import views
from user.views import signin, signup


urlpatterns = [
    path('logout/', views.Logout.as_view(), name = 'logout'),
    path('signin/', signin, name = 'signin'),
    path('signup/', signup, name = 'signup'),
    path('', views.index, name = 'index' ),
    path('<slug:slug>/', views.post, name = 'post'),

    
]