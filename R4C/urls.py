from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
    path('excel/', include('orders.urls'))
]
