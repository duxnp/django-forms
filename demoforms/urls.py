from django.urls import path

from .views import CommenFormView, CommentListView

urlpatterns = [
    path("comment", CommenFormView.as_view(), name="comment"),
    path("comments", CommentListView.as_view(), name="comments"),
]
