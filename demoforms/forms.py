from django import forms
from django.core.exceptions import ValidationError

from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(required=True, label="Your name", max_length=100)
    comment = forms.CharField(
        required=True, widget=forms.Textarea(attrs={"rows": 10, "cols": 80})
    )

    def log_data(self):
        print(self.cleaned_data.get("name"))
        print(self.cleaned_data.get("comment"))


class CommentModelForm(forms.ModelForm):
    template_name = "form_snippet.html"

    class Meta:
        model = Comment
        fields = {"name", "comment"}
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Enter your name", "class": "standard-input"}
            ),
            "comment": forms.Textarea(
                attrs={
                    "placeholder": "What is your comment?",
                    "class": "standard-area",
                    "rows": 10,
                    "cols": 80,
                }
            ),
        }

    def clean_name(self):
        print("form clean name")
        name = self.cleaned_data.get("name")
        if name == "reject":
            raise ValidationError("name has been rejected")
        return name

    def clean(self):
        print("form clean")
        cleaned_data = super().clean()
        print(cleaned_data)
        name = cleaned_data.get("name")
        comment = cleaned_data.get("comment")

        if name and name.startswith("t") and comment and not comment.startswith("c"):
            raise ValidationError(
                "Name starts with a t, so comment must start with a c."
            )
