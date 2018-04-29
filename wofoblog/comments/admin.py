from django.contrib import admin
from .models import Comment
# Register your models here.
# class CommitAdmin(admin.ModelAdmin):
#     list_display = ('to_blog_id', 'from_id', 'user_name', 'time_commit')
#     list_filter = ('to_blog_id', 'from_id', 'user_name',)
#     search_fields = ('to_blog_id',)
#
# admin.site.register(Comment, CommitAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('number_commit', 'user_name', 'from_id', 'level')

admin.site.register(Comment, CommentAdmin)
