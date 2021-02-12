from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


class ArticleTag(models.Model):
    """
    Taguri pentru clasificat si filtrat articole.

    ex: 'internship', 'hackathon', 'python', 'java', 'conference', etc.
    """

    name = models.TextField(null=False, blank=False, help_text="the tag shortname")
    description = models.TextField(
        null=False, blank=False, help_text="the tag explanaition"
    )
    color = models.TextField(
        null=False,
        blank=False,
        help_text="the tag's color, may be useful to keep consistency on fe, ex: 'blue",
    )

    def __str__(self):
        return self.name


class Article(models.Model):
    """Default article model for Portfolio Manager for Companies.

    An article can be anything from an internship, hackathon, other announcements.
    """

    def __str__(self):
        return self.title

    # Each article must have atleast an author, a title and some content.
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        help_text="article author",
    )
    title = models.TextField(null=False, blank=False, help_text="the article title")
    content = models.TextField(null=False, blank=False, help_text="the article content")
    short_description = models.TextField(
        null=False,
        blank=False,
        help_text="short description of the company, appears in list of companies",
    )

    # The date the article was created
    created_date = models.DateTimeField(
        auto_now_add=True, help_text="Date the article was created"
    )

    # The date the article will be published (if it is approved by this date)
    # If not approved by this date, then it should be published as soon as it's approved
    publish_date = models.DateTimeField(help_text="Date the article was published")

    # The date the article will no longer be available (deadline for submitting applications)
    expiration_date = models.DateTimeField(
        null=True,
        blank=True,  # If ommited we assume it doesn't expire
        help_text="Valid until date",
    )

    is_approved = models.BooleanField(
        default=False, help_text="was this approved by an admin for publishing"
    )

    is_pinned = models.BooleanField(
        default=False, help_text="should be displayed in the pinned articles section"
    )

    university_public_note = models.TextField(
        null=True,
        blank=True,
        help_text="Informatii publice adaugate de universitate pentru acest articol",
    )
    university_private_note = models.TextField(
        null=True,
        blank=True,
        help_text="Informatii private adaugate de universitate pentru acest articol",
    )

    tags = models.ManyToManyField(ArticleTag)

    history = HistoricalRecords()

    def get_absolute_url(self):
        """Used to generate reverse URL for detail page by forms."""
        return reverse("articles:detail", kwargs={"pk": self.pk})
