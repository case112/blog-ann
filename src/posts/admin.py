from django.contrib import admin

from . models import Author, Category, Post, Comment, Page

class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'slug', 'overview', 'content', 'thumbnail', 'cover_photo', 'categories', 'featured', 'status']

    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    actions = ['publish_post']
    prepopulated_fields = {'slug': ('title',)}

    def publish_post(self, request, queryset):
        queryset.update(status=1)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'comment', 'post', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date')
    search_fields = ('name', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved_comment=True)


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Page)

