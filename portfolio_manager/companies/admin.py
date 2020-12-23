from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from portfolio_manager.companies import models

admin.site.register(models.Company, SimpleHistoryAdmin)
