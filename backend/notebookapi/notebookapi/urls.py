"""notebookapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customauthentication import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.UserView.as_view()),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('verify/', views.LoginUserApi.as_view()),
    path('verif/', views.VarifyUser.as_view()),
    path('notes/', views.UsersNotes.as_view()),
    path('postnotes/', views.NotesPost.as_view()),
    path('deletenotes/<int:pk>/', views.NotesDelete.as_view()),
    path('foreditget/', views.GetNoteForEdit.as_view()),
    path('foreditget/<int:pk>/', views.GetNoteForEdit.as_view()),
    path('edituser/', views.UserEditView.as_view()),
]
