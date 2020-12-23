from datetime import datetime

from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from portfolio_manager.articles.models import Article


class ArticleUserPassesTestMixin(UserPassesTestMixin):
    """Permission gatekeeper for articles

    Only allow admin and people from the respective company access to views
    that inherit from this mixin.
    """

    def test_func(self):
        # Admins can edit anything
        if self.request.user.is_superuser:
            return True

        user_company = self.request.user.company

        # People without a company can't edit anything!
        if not user_company:
            return False

        article_instance = Article.objects.get(id=self.kwargs["pk"])

        # Maybe somebody tried an invalid or expired URL
        if not article_instance:
            return False

        # Logged in user should only be able to edit it's own company's articles
        return user_company.pk == article_instance.company.pk

    def handle_no_permission(self):
        """Where to redirect if request couldn't be authenthicated in test_func."""
        return redirect("home")  # Maybe add an invalid access page here?


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"
    slug_field = "article"
    slug_url_kwarg = "article_id"


article_detail_view = ArticleDetailView.as_view()


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(
        Q(is_approved=True),
        Q(publish_date__lte=datetime.now()),
        # Has no expiration date or has not expired yet
        Q(expiration_date__isnull=True) | Q(expiration_date__lte=datetime.now()),
    )
    paginate_by = 10
    template_name = "articles/article_list.html"


article_list_view = ArticleListView.as_view()


class ArticleCompanyListView(ArticleListView):
    queryset = Article.objects.all()  # TODO filter by company
    template_name = "articles/article_company_list.html"


article_company_list_view = ArticleCompanyListView.as_view()


class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "content", "publish_date", "expiration_date"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.is_approved = False

        return super().form_valid(form)


article_create_view = ArticleCreateView.as_view()


class ArticleUpdateView(ArticleUserPassesTestMixin, UpdateView):
    model = Article
    fields = ["title", "content", "publish_date", "expiration_date"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.is_approved = False

        return super().form_valid(form)


article_update_view = ArticleUpdateView.as_view()


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("articles:list")


article_delete_view = ArticleDeleteView.as_view()
