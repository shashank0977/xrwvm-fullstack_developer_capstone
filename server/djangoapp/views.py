from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

from .restapis import get_request, post_review


@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({
            "userName": username,
            "status": "Authenticated"
        })

    return JsonResponse({
        "userName": username,
        "status": "Invalid credentials"
    }, status=401)


@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"status": "Logged out"})


@csrf_exempt
def registration(request):
    data = json.loads(request.body)

    username = data["userName"]
    password = data["password"]

    if User.objects.filter(username=username).exists():
        return JsonResponse(
            {"error": "Username already exists"},
            status=400
        )

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=data.get("firstName", ""),
        last_name=data.get("lastName", ""),
        email=data.get("email", "")
    )

    return JsonResponse({
        "userName": user.username,
        "status": "Registered"
    })


def get_dealerships(request):
    return JsonResponse(
        get_request("/fetchDealers"),
        safe=False
    )


def get_dealers_by_state(request, state):
    return JsonResponse(
        get_request(f"/fetchDealers/{state}"),
        safe=False
    )


def get_dealer_details(request, dealer_id):
    return JsonResponse(
        get_request(f"/fetchDealer/{dealer_id}")
    )


def get_dealer_reviews(request, dealer_id):
    return JsonResponse(
        get_request(f"/fetchReviews/dealer/{dealer_id}"),
        safe=False
    )


@csrf_exempt
def add_review(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST required"},
            status=400
        )

    data = json.loads(request.body)
    result = post_review(data)

    return JsonResponse(result)
