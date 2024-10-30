
from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'screenshot', views.ScreenshotViewSet, basename='screenshot')  # Add this line

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    path('admin/', admin.site.urls),
]
