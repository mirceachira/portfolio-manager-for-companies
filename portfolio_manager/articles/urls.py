from django.urls import path

from portfolio_manager.articles import views

app_name = "users"
urlpatterns = [
    path("", views.article_list_view, name="list"),
    path("<str:pk>/", views.article_detail_view, name="detail"),
]
