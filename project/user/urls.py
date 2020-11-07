from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewset


router = SimpleRouter()
router.register('users', UserViewset, basename='users')

urlpatterns = router.urls