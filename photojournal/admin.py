from django.contrib import admin
from . models import Post, Comment, Category


@admin.register(Post)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("message__startswith", )
    fields = ("author", "photo", "message", 'slug', 'publication', 'category')


admin.site.register(Comment)
admin.site.register(Category)