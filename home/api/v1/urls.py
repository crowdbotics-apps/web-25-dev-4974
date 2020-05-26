from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomTextViewSet,
    GFFViewSet,
    GVfdfgViewSet,
    HomePageViewSet,
    ShghgViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("shghg", ShghgViewSet)
router.register("gvfdfg", GVfdfgViewSet)
router.register("gff", GFFViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
