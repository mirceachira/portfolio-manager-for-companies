from django.urls import path

from portfolio_manager.articles import views

app_name = "users"
urlpatterns = [
    path("list", views.article_list_view, name="list"),
    path("company_list", views.article_company_list_view, name="company-list"),
    path("detail/<str:pk>/", views.article_detail_view, name="detail"),
    path("add/", views.article_create_view, name="add"),
    path("update/<str:pk>/", views.article_update_view, name="update"),
    path("delete/<str:pk>/", views.article_delete_view, name="delete"),
]
