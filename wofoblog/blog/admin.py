from django.contrib import admin

# Register your models here.

from .models import User_info, Tag, Blog

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)
    list_filter = ('tag_name',)
    search_fields = ('tag_name',)


class User_infoAdmin(admin.ModelAdmin):
    list_display = ('user_number', 'name', 'email',)
    list_filter = ('name',)
    search_fields = ('name',)



class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_number', 'title', 'create_data', 'blog_tag',)
    list_filter = ('title', 'blog_tag', 'create_data', 'author',)
    search_fields = ('title', 'blog_tag', 'create_data', 'author',)

admin.site.register(User_info, User_infoAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)

