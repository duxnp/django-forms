from django.urls import path
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .views import CommenFormView, CommentListView

# Example of using the csrf_protect decorator like a function (which is pretty much what decorators are anyway)
# path("comment", csrf_protect(CommenFormView.as_view()), name="comment"),

urlpatterns = [
    path("comment", CommenFormView.as_view(), name="comment"),
    path("comments", CommentListView.as_view(), name="comments"),
]
