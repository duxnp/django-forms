from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import CommentForm, CommentModelForm
from .models import Comment


class CommenFormView(FormView):
    template_name = "comment.html"
    form_class = CommentModelForm
    success_url = "comment"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CommentListView(ListView):
    model = Comment
    context_object_name = "comment_data"

    def render_to_response(
        self, context: dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        # return super().render_to_response(context, **response_kwargs)
        comments = ""
        for comment in context["comment_data"]:
            comments += f"<li>{comment.name}---{comment.comment}</li>"
        return HttpResponse(f"<html><body><ul>{comments}</ul></body></html>")
