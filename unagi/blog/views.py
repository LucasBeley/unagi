from django.views.generic import DetailView, ListView

from .models import Post


class IndexView(ListView):
    """Actually a PostListView, to show latest posts and allow to navigate through pages."""

    model = Post
    paginate_by = 3
    ordering = "-posted_at"
    template_name = "blog/index.html"
    
    def get_queryset(self):
        return super().get_queryset().filter(posted_at__isnull=False, hidden_at__isnull=True)
    
class PostView(DetailView):
    """View for displaying a single post."""
    
    model = Post
    template_name = "blog/post.html"
    
    def get_queryset(self):
        return super().get_queryset().filter(posted_at__isnull=False, hidden_at__isnull=True)
