from django.db import models
from django.core.validators import RegexValidator, MaxLengthValidator


class Comment(models.Model):
    name = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        validators=[
            RegexValidator(
                regex="^[a-zA-Z]*$",
                message="Name must be alpha characters only",
                code="invalid_name",
            )
        ],
    )
    comment = models.TextField(
        null=True,
        blank=True,
        validators=[
            MaxLengthValidator(limit_value=10, message="Your message is way too long!")
        ],
    )
