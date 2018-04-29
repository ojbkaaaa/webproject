from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
import hashlib
# from ..static.ckeditor.ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


from django.core.validators import RegexValidator
from django.core.validators import EmailValidator,URLValidator,DecimalValidator,MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator

# Create your models here.

class User_info(models.Model):
    user_number = models.AutoField(primary_key=True, verbose_name='用户编号')
    name = models.CharField(max_length=10, verbose_name='用户')
    pwd = models.CharField(max_length=20, verbose_name='密码')
    headImg = models.ImageField(upload_to='headImg/', null=True, default='headImg/uiface2.png')
    email = models.EmailField(verbose_name='邮箱')
    phone = models.CharField(max_length=11, verbose_name='手机号', error_messages={
        'one':'不能为空',
        'two':'格式错误',
    },validators=[
        RegexValidator(regex='', message='不能为空',code='one'),
        RegexValidator(regex='^((1[3,5,8][0-9])|(14[5,7])|(17[0,6,7,8])|(19[7]))\\d{8}$', message='格式错误', code='two'),
    ]) # 需要对手机进行验证
    common = models.CharField(max_length=100, null=True, verbose_name='个人说明', blank=True) # 可以为空
    def __str__(self):
        return self.name

    def is_authenticated(self):
        return True

    def hashed_password(self, password=None):
        if not password:
            return self.pwd
        else:
            return hashlib.md5(password).hexdigest()

    def check_password(self, password):
        if self.hashed_password(password) == self.pwd:
            return True
        return False
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

class Tag(models.Model):
    tag_name = models.CharField(max_length=50,verbose_name='标签')
    def __str__(self):
        return self.tag_name
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        pass

class Blog(models.Model):
    blog_number = models.AutoField(primary_key=True, verbose_name='博文编号')
    title = models.CharField(max_length=100, verbose_name='标题')
    blog_content = RichTextField(verbose_name='博客内容',config_name='default')

    create_data = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    author = models.ManyToManyField('User_info',  verbose_name='作者')
    # blog_image = models.ImageField(upload_to='img', null=True, verbose_name='图片', blank=True)
    blog_tag = models.ForeignKey(Tag, on_delete=None, verbose_name='标签')
    blog_excerpt = models.CharField(max_length=200, blank=True)  # 摘要
    views = models.PositiveIntegerField(default=0)  # 记录阅读人数

    def add_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def blog_excerpt_save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.blog_excerpt:
            self.blog_excerpt = strip_tags(self.blog_content)[:200]
            # 调用父类的 save 方法将数据保存到数据库中
            super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'blog_number': self.blog_number})

    class Meta:
        verbose_name = '博文'
        verbose_name_plural = '博文'








