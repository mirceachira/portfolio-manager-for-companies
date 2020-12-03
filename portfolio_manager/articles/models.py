from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    """Default article model for Portfolio Manager for Companies.

    An article can be anything from an internship, hackathon, other announcements.
    """

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

    # The date the article was created
    created_date = models.DateTimeField(
        auto_now_add=True, help_text="Date the article was created"
    )

    # The date the article will be published (if it is approved by this date)
    # If not approved by this date, then it should be published as soon as it's approved
    publish_date = models.DateTimeField(help_text="Date the article was published")

    is_approved = models.BooleanField(
        help_text="was this approved by an admin for publishing"
    )
