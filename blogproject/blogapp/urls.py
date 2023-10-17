from django.urls import path
from . import views
from .views import UserList,BlogList

urlpatterns = [
    path('', views.home),
    path('register/', views. loginpage),
    path('reg/', views.Registration),
    path('login/', views.login),
    path('viewblog/', BlogList.as_view()),
    path('homepage/', views.homepage),
    path('adminhome/', views.adminhome),
    path('postblog/', views.postblog),
    path('display/', UserList.as_view()),
    path('deleteuser/<int:id>/', views.deleteuser),
    path('updateuser/<int:id>/',views.updateuser),
    path('updateuserform/', views.updateuserform),
    path('postnewblog/', views.postnewblog),
    path('userpostedblogs/', views.userpostedblogs),
    path('editblog/<int:id>',views.editblog),
    path('postupdateblog/',views.postupdateblog),
    path('deleteBlog/<int:id>',views.deleteBlog),
    path('edituserprofile/<int:id>', views.edituserprofile),
    path('edituserform/', views.edituserform),


]