from account.views import favoriteStatus
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("link/<int:articleId>", views.link, name="link"),
    path("dashboard",views.dashboard, name="dashboard"),
    path("happiness", views.happiness, name="happiness"),
    path("food", views.food, name="food"),
    path("food/generate", views.generateMeal, name="generate"),
    path("favoriteStatus/<int:foodId>", views.favoriteStatus, name="favoriteStatus")
]
