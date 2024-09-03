from django.contrib import admin, messages
from django.contrib.auth.models import Group, User
from django.utils import timezone
from django.utils.translation import ngettext as _

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_online",
        "posted_at",
        "hidden_at",
        "created_at",
        "updated_at",
    )
    fields = ("content", "title", "cover_image_url")
    readonly_fields = ("created_at", "updated_at", "posted_at")
    actions = ("make_published", "make_hidden")

    class Media:
        css = {"all": ("blog/admin.css",)}

    @admin.action(description="Make selected posts published")
    def make_published(self, request, queryset):
        """Admin action to mark selected posts as published."""

        updated = queryset.update(posted_at=timezone.now(), hidden_at=None)
        self.message_user(
            request,
            _(
                "%d story was successfully marked as published.",
                "%d stories were successfully marked as published.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Make selected posts hidden")
    def make_hidden(self, request, queryset):
        """Admin action to mark selected posts as hidden."""

        updated = queryset.update(hidden_at=timezone.now())
        self.message_user(
            request,
            _(
                "%d story was successfully marked as hidden.",
                "%d stories were successfully marked as hidden.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    def get_form(self, request, obj=None, **kwargs):
        """Customize the form to make the content textarea larger."""
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["content"].widget.attrs["cols"] = "100"
        form.base_fields["content"].widget.attrs["style"] = "width: 99%"
        form.base_fields["content"].widget.attrs["rows"] = "120"
        return form


admin.site.unregister(Group)
admin.site.unregister(User)
