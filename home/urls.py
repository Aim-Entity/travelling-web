from django.urls import path, include
from . import views
from service.views import LocationSerializers
from rest_framework import routers

router = routers.DefaultRouter()

router.register("newsletter", views.NewsletterSubscriptionView)


urlpatterns = [
    path("", views.index, name="home"),
    path("api/", include(router.urls)),
]
