from django.contrib import admin

from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','status','published_date','created_date')
    list_filter = ('category',)
    search_fields = ('title',)

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)