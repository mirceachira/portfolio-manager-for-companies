from django.urls import path

from portfolio_manager.companies import views

app_name = "users"
urlpatterns = [
    path("list/", views.company_list_view, name="list"),
    path("detail/<str:pk>/", views.company_detail_view, name="detail"),
    path("articles/<str:pk>/", views.company_article_list_view, name="articles"),
]
