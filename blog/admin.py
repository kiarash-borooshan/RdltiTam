from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostDecor(admin.ModelAdmin):
    list_display = ("title", "author", "status", "publish", "updated", "created")
    prepopulated_fields = {
        "slug": ("title", "author")
    }
    list_filter = ("status", "publish", "created", "author")
    search_fields = ("title", "body")
    # raw_id_fields = ("author", )
    date_hierarchy = "publish"
    list_editable = ("status", )
    list_display_links = ("author", )
