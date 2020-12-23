from datetime import datetime

from django.db.models import Q
from django.views.generic import DetailView, ListView

from portfolio_manager.articles.models import Article
from portfolio_manager.companies.models import Company


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
