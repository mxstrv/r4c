from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
    path('robots/', include('robots.urls'))
]
