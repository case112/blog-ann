from django.contrib import admin

from . models import Author, Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','timestamp')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
