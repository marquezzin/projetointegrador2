"""
URL configuration for the platform.
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # API routes will be added here as apps are built
    # path('api/v1/accounts/', include('apps.accounts.urls')),
    # path('api/v1/content/', include('apps.content.urls')),
    # path('api/v1/submissions/', include('apps.submissions.urls')),
    # path('api/v1/progress/', include('apps.progress.urls')),
    # path('api/v1/classgroups/', include('apps.classgroups.urls')),
]
