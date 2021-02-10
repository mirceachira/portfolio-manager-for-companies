from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from portfolio_manager.articles import models

admin.site.register(models.ArticleTag, SimpleHistoryAdmin)
admin.site.register(models.Article, SimpleHistoryAdmin)
