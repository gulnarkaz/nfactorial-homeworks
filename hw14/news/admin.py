from django.contrib import admin
from .models import News, Comment

 
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'has_comments')
    inlines = [CommentInline] 
    
    def has_comments(self, obj):
        return obj.has_comments()
    has_comments.boolean = True
    has_comments.short_description = 'Has comments'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'content', 'created_at')
    list_filter = ('news',)
    
