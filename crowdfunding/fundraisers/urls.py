
from django.urls import path
from . import views

urlpatterns = [
    path('fundraisers/', views.FundraiserList.as_view()),
    path('fundraisers/<int:pk>/', views.FundraiserDetail.as_view()),
    path('pledges/', views.PledgesList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
]