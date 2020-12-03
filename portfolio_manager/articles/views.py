from datetime import datetime

from django.views.generic import DetailView, ListView

from portfolio_manager.articles.models import Article


class ArticleDetailView(DetailView):

    model = Article
    template_name = "articles/article_detail.html"
    slug_field = "article"
    slug_url_kwarg = "article_id"


article_detail_view = ArticleDetailView.as_view()


class ArticleListView(ListView):

    model = Article
    queryset = Article.objects.filter(
        is_approved=True, publish_date__lte=datetime.now()
    )
    paginate_by = 10
    template_name = "articles/article_list.html"


article_list_view = ArticleListView.as_view()
