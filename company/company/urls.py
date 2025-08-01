"""
URL configuration for company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from users import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sections.dashboard.urls')),
    path('post/', include('sections.blog.urls')),
    path('chat/', include('sections.chat.urls')),
    path('group/', include('sections.groups.urls')),
    path('market/', include('sections.market.urls')),
    path('audio/', include('sections.audio.urls')),
    path('archive/', include('sections.archive.urls')),
    path('inbox/', include('sections.notifications.urls')),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", views.user_logout, name="logout"),
    # path("profile/", views.profile, name="profile"),
    path("profile/<slug:slug>/", views.profile, name="profile"),
    path("profile_edit/", views.edit_profile, name="edit-profile"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

