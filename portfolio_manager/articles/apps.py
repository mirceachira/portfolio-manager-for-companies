from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArticlesConfig(AppConfig):
    name = "articles"
    verbose_name = _("Articles")

    def ready(self):
        try:
            import portfolio_manager.articles.signals  # noqa F401
        except ImportError:
            pass
