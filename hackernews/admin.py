from django.contrib import admin
from hackernews.models import User, Profile, News, Comment

class CommentInLine(admin.TabularInline):
    model = Comment


class NewsAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment)

