from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, CharField, ForeignKey
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from portfolio_manager.companies.models import Company


class User(AbstractUser):
    """Default user for Portfolio Manager for Companies."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    company = ForeignKey(Company, null=True, blank=True, on_delete=CASCADE)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
