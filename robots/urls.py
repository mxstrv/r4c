from django.urls import path

from robots.views import download_excel_file

urlpatterns = [
    path('download/', download_excel_file, name='download_excel')
]
