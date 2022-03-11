from django.urls import path
from .views import StaffList, StaffDetail

urlpatterns = [
    path('<int:pk>/', StaffDetail.as_view()),
    path('', StaffList.as_view())
]