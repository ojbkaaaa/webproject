from django.template import Library
from ..models import User_info, Tag, Blog

register = Library()
@register.simple_tag
def get_blog_num(num=5):# 前台展示数量
    # {% get_blog_num as blog_num %}模板标签获取到最新文章列表，然后我们通过 as 语法（Django 模板系统的语法）
    # 将获取的文章列表保存进了 recent_post_list 模板变量中，之后就可以通过 for 循环来循环显示文章列表数据
    #一定要as语法，不然显示的不是blog.title对象
    post_num = Blog.objects.all().order_by('-create_data')[:5]
    # print(post_num)
    # for i in post_num:
    #     return i.title
    return post_num
    pass

@register.simple_tag
def get_session(request):
    session = request.session.get('username')
    return session




