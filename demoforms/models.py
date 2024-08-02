from collections.abc import Collection
from typing import Any
from django.db import models
from django.core.validators import RegexValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_max_length(value):
    if value and len(value) > 10:
        raise ValidationError(
            "%(value)s is over 10 characters in length.",
            params={"value": value},
        )


@deconstructible
class OurMaxLengthValidator:
    max = 0

    def __init__(self, max=None) -> None:
        self.max = max

    def __call__(self, value) -> Any:
        if value and len(value) > self.max:
            raise ValidationError(
                f"{value} - Must not be over {self.max} characters in length.",
                code="max_value_error",
            )

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            return NotImplemented
        return self.max == value.max


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
            # MaxLengthValidator(limit_value=10, message="Your message is way too long!")
            # validate_max_length
            OurMaxLengthValidator(max=10)
        ],
    )

    def clean(self):
        print("model clean")
        return super().clean()

    def clean_fields(self, exclude: Collection[str] | None = ...):
        print("model clean fields")
        return super().clean_fields(exclude)
