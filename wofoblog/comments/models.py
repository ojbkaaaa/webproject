from django.db import models
from mptt.models import MPTTModel

# Create your models here.
# class Comment(models.Model):
#     number_commit = models.AutoField(primary_key=True, verbose_name='评论id')
#     to_blog_id = models.ForeignKey('blog.Blog', to_field='blog_number', on_delete=None, verbose_name='关联博文id')
#     blog_commit = models.TextField(verbose_name='评论内容')
#     user_name = models.CharField(max_length=50, blank=True, null=True)
#     from_id = models.ForeignKey('self', blank=True, null=True, on_delete=None, default=None, verbose_name='回复用户')
#     time_commit = models.DateField(auto_now_add=True, verbose_name='创建日期')
#     def __str__(self):
#         if self.from_id is not None:
#             return '%s回复了%s' % (self.user_name, self.from_id.user_name)
#         return '%s 评论文章 post_%s' % (self.user_name, str(self.to_blog_id))
#     class Meta:
#         verbose_name = '评论'
#         verbose_name_plural = '评论'

class Comment(MPTTModel):
    number_commit = models.AutoField(primary_key=True, verbose_name='评论id')
    to_blog_id = models.ForeignKey('blog.Blog', to_field='blog_number', on_delete=None, verbose_name='关联博文id')
    blog_commit = models.TextField(verbose_name='评论内容')
    user_name = models.CharField(max_length=50, blank=True, null=True)
    from_id = models.ForeignKey('self', blank=True, null=True, on_delete=None, default=None, verbose_name='回复用户', related_name='children')
    time_commit = models.DateField(auto_now_add=True, verbose_name='创建日期')
    def __str__(self):
        if self.from_id is not None:
            return '%s回复了%s' % (self.user_name, self.from_id.user_name)
        return '%s 评论文章 %s' % (self.user_name, str(self.to_blog_id))
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

    class MPTTMeta:
        parent_attr = 'from_id'


# class UserNotificationsCount(models.Model):
#     """这个Model保存着每一个用户的未读消息数目"""
#     user_id = models.ForeignKey('blog.User_info', verbose_name='用户')
#     unread_count = models.IntegerField(default=0)
#     def __str__(self):
#         return '%s回复了你: %s' % (self.user_id, self.unread_count)