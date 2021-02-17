from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'content')
    prepopulated_fields = {'slug': ('name',)} # new

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
# admin.site.register(Post)