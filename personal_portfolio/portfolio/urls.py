from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SkillViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("skills", SkillViewSet)
#router.register("about", AboutViewSet)   # optional, if you made it

urlpatterns = [
    path("api/", include(router.urls)),
]
