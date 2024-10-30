from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from main.serializers import UserSerializer, GroupSerializer, ScreenshotRequestSerializer
from playwright.sync_api import sync_playwright
from io import BytesIO
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    print("VIEWSET ACESSADO")
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    print("GROUP VIEWSET ACESSADO")
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# viewsets.ModelViewSet
# class ScreenshotView(APIView):
class ScreenshotView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request):
        # Return a simple response for GET requests
        return Response({
            "message": "Please use POST method with the following format",
            "example": {
                "url": "https://www.google.com",
                "viewport_width": 1200,
                "viewport_height": 800,
                "full_page": True
            }
        })

    def post(self, request):
        serializer = ScreenshotRequestSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            viewport_width = serializer.validated_data['viewport_width']
            viewport_height = serializer.validated_data['viewport_height']
            full_page = serializer.validated_data['full_page']

            # Use Playwright to capture the screenshot
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page(
                    viewport={"width": viewport_width, "height": viewport_height}
                )
                page.goto(url)
                screenshot = page.screenshot(full_page=full_page, type="png")
                browser.close()

            # Prepare the screenshot for HTTP response
            response = HttpResponse(screenshot, content_type="image/png")
            response['Content-Disposition'] = 'attachment; filename="screenshot.png"'
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
