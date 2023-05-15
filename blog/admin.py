from django.contrib import admin
from blog.models import blog_model

# Register your models here.

#admin.site.register(blog_model)


@admin.register(blog_model)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on', 'status']
    sortable_by = ['created_on']
    list_filter = ['status']
    search_fields = ['title', 'author']




