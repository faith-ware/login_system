from django.urls import path
from .views import login, signup,logout,userEdit, userDelete
app_name = "accounts"

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("signup/", signup, name="signup"),
    path("<int:id>/update/", userEdit, name="useredit"),
    path("<int:id>/delete/", userDelete, name="userdelete")
]
