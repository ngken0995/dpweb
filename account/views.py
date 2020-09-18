
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Calorie, User, Article, Happiness, Personal, Favorite
from .forms import HappinessForm

# Create your views here.
@csrf_exempt
def favoriteStatus(request, foodId):
    if request.method == "GET":
        if Favorite.objects.filter(user = request.user, food_id = foodId).exists():
            return JsonResponse({'status': True})
        else:
            return JsonResponse({'status':False})
    elif request.method == "POST":
        favorite = Favorite()
        data = json.loads(request.body)
        favorite.user = request.user
        favorite.calories = data["calories"]
        favorite.carbs = data["carbs"]
        favorite.fat = data["fat"]        
        favorite.food_id = foodId
        favorite.image = data["image"]
        favorite.protein = data["protein"]
        favorite.title = data["title"]
        favorite.save()
        return JsonResponse({"message": "Favorite sent successfully."})
    elif request.method == "DELETE":
        Favorite.objects.filter(user=request.user, food_id = foodId).delete()
        return JsonResponse({"message": "Deleted successfully."})



def food(request):
    return render(request, "account/food.html")

def generateMeal(request):
    personal = Personal.objects.get(user=request.user)
    calorieRow = Calorie.objects.get(age=personal.age, gender=personal.gender)
    calorie = 500
    if personal.activeLevel == 's':
        calorie = calorieRow.sedentary
    if personal.activeLevel == 'm':
        calorie = calorieRow.moderatelyActive
    if personal.activeLevel == 'a':
        calorie = calorieRow.active

    threeMeals= calorie/3
    minValue = threeMeals - 100
    maxValue = threeMeals + 100

    if request.method == "GET":
        return JsonResponse({'min': minValue, 'max': maxValue})

def dashboard(request):
    if Happiness.objects.filter(user = request.user).exists():
        recentTime = Happiness.objects.filter(user = request.user).order_by('-timestamp').first().timestamp
        now = timezone.now()
        ask = recentTime + timezone.timedelta(hours=2) < now
        return render(request, "account/dashboard.html", {
            "form":HappinessForm(),
            "ask":ask
        })
    else:
        ask = True
        return render(request, "account/dashboard.html", {
            "form":HappinessForm(),
            "ask":ask
        })

def index(request):
    articles = Article.objects.all().order_by('-timestamp')[:2]
    return render(request, "account/index.html", {
        "articles":articles
    })

def happiness(request):
    if request.method == "POST":
        form = HappinessForm(request.POST)
        if form.is_valid():
            happiness = Happiness()
            happiness.user = request.user
            happiness.scale = form.cleaned_data["scale"]
            happiness.save()
            return HttpResponseRedirect(reverse("dashboard"))

def link(request, articleId):    
    article = get_object_or_404(Article, id = articleId)
    
    if article.link is not None:
        return redirect(f'{article.link}')

    
    return render(request, "account/article.html", {
        "article":article
    })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render(request, "account/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "account/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "account/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            personal = Personal()
            personal.user = user
            personal.age = request.POST["age"]
            personal.gender = request.POST["gender"]
            personal.activeLevel = request.POST["activeLevel"]
            personal.save()
        except IntegrityError:
            return render(request, "account/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "account/register.html")
