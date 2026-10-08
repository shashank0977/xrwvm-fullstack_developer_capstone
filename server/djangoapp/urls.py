from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "djangoapp"

urlpatterns = [
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.registration, name="register"),
    path("dealers", views.get_dealerships, name="dealers"),
    path("dealers/<str:state>", views.get_dealers_by_state, name="dealers_by_state"),
    path("dealer/<int:dealer_id>", views.get_dealer_details, name="dealer"),
    path("dealer/<int:dealer_id>/reviews", views.get_dealer_reviews, name="reviews"),
    path("review", views.add_review, name="review"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
