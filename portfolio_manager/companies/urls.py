from django.urls import path

from portfolio_manager.companies import views

app_name = "users"
urlpatterns = [
    path("", views.company_list_view, name="list"),
    path("<str:pk>/", views.company_detail_view, name="detail"),
]
