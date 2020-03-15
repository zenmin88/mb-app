from django.contrib import admin

from posts.models import Post


# class PostAdmin(admin.ModelAdmin):
#     list_display = ['text']
# admin.site.register(Post, PostAdmin)


admin.site.register(Post)
