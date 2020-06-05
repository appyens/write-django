from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'publish', 'views', 'post_tags')
    #
    # def get_tags(self):
    #     pass


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment)
