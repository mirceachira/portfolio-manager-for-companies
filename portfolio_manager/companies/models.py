from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


class Company(models.Model):
    "Default Company Model for Portfolio Manager for Companies"

    # Each company has a name, description, contact email/phone, and adress
    name = models.TextField(null=False, blank=False, help_text="company's name")
    description = models.TextField(
        null=False, blank=False, help_text="description of the company"
    )

    email = models.EmailField(null=False, blank=False, help_text="company's email")
    phone = models.TextField(null=True, blank=True, help_text="company's phone")
    adress = models.TextField(
        null=False,
        blank=False,
        help_text="adresa fizica (de preferat din Cluj) a companiei",
    )

    website = models.URLField(
        max_length=200, null=True, blank=True, help_text="website-ul companiei"
    )
    facebook = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        help_text="pagina de facebook a companiei",
    )
    linkdin = models.URLField(
        max_length=200, null=True, blank=True, help_text="pagina de linkdin a companiei"
    )

    has_gold_status = models.BooleanField(
        default=False, help_text="company is a valued partener of our university"
    )

    university_public_note = models.TextField(
        null=True,
        blank=True,
        help_text="Informatii publice adaugate de universitate pentru aceasta companie",
    )
    university_private_note = models.TextField(
        null=True,
        blank=True,
        help_text="Informatii private adaugate de universitate pentru aceasta companie",
    )

    history = HistoricalRecords()

    def get_absolute_url(self):
        """Used to generate reverse URL for detail page by forms."""
        return reverse("companies:detail", kwargs={"pk": self.pk})
