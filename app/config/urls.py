"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
1. Add an import: from my_app import views
2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
1. Add an import: from other_app.views import Home
2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
path("", lambda request: HttpResponse("✅ API is running - see /api/docs/ for Swagger UI")),

# --- Admin ---
path("admin/", admin.site.urls),

# --- Inertia Frontend ---
# path("", include("frontend.urls")), # TODO: add when Inertia frontend is ready

# # --- Classic Views ---
# path("pages/", include("core.urls")), # example

# --- API ---
path("api/", include("api.urls")),

# --- API Schema & Docs ---
path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
