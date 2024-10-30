
from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework import routers

router = routers.DefaultRouter();
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'screenshots', views.ScreenshotView)

urlpatterns = [
    path('', include(router.urls)),
    # path('screenshot/', views.ScreenshotView.as_view(), name='screenshot'),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    path('admin/', admin.site.urls),
]
