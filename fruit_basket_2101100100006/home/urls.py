from django.urls import path,include
from home import views


urlpatterns = [
    
    path('', views.index, name='home'),
    path('about',views.about, name='about'),
    path('login',views.login, name='login'),
    path('logout',views.logoutUser, name='logout'),
    path('register',views.register,name='register'),
    path('add',views.add,name='add'),
    path('<id>/update',views.update,name='update'),
    path('<id>/delete',views.delete,name='delete'),
    path('<id>/buy',views.buy,name='buy')
    
]