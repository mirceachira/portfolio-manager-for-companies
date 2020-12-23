from datetime import datetime

from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView

from portfolio_manager.articles.models import Article
from portfolio_manager.companies.models import Company


class CompanyUserPassesTestMixin(UserPassesTestMixin):
    """Permission gatekeeper for company

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

        company_instance = Company.objects.get(id=self.kwargs["pk"])

        # Maybe somebody tried an invalid or expired URL
        if not company_instance:
            return False

        # Logged in user should only be able to edit it's own companies
        return user_company.pk == company_instance.pk

    def handle_no_permission(self):
        """Where to redirect if request couldn't be authenthicated in test_func."""
        return redirect("home")  # Maybe add an invalid access page here?


class CompanyDetailView(DetailView):
    model = Company
    template_name = "companies/company_detail.html"


company_detail_view = CompanyDetailView.as_view()


class CompanyListView(ListView):
    model = Company
    paginate_by = 10
    template_name = "companies/company_list.html"


company_list_view = CompanyListView.as_view()


class CompanyArticlesListView(ListView):
    template_name = "companies/company_article_list.html"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return Article.objects.filter(
            Q(id=self.kwargs["pk"]),
            Q(is_approved=True),
            Q(publish_date__lte=datetime.now()),
            # Has no expiration date or has not expired yet
            Q(expiration_date__isnull=True) | Q(expiration_date__lte=datetime.now()),
        )


company_article_list_view = CompanyArticlesListView.as_view()


class CompanyUpdateView(CompanyUserPassesTestMixin, UpdateView):
    model = Company
    fields = [
        "name",
        "description",
        "adress",
        "phone",
        "email",
        "linkdin",
        "facebook",
        "website",
    ]


article_update_view = CompanyUpdateView.as_view()
