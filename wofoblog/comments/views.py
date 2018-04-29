from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Comment
import json
from blog.models import Blog
# Create your views here.

def comment(request): # 评论时ajax异步传递数据
    session = request.session.get("username")
    if session:
        blog_commit = request.POST.get("blog_commit")# 获取评论内容
        blog_id = request.POST.get("number_commit")
        blog_detail = get_object_or_404(Blog, pk=blog_id)
        Comment.objects.create(to_blog_id=blog_detail, blog_commit=blog_commit, user_name=session)
        print("评论成功")
        return HttpResponse(json.dumps("评论成功"))
        pass
    else:
        return HttpResponse(json.dumps("请登录后再评论！！！"))

    pass


def add(request):
    username = request.session.get('username')
    if request.method == 'POST':
        if username:
            if request.is_ajax:
                print(request.POST)
                # print("1515151")
                number_commit = request.POST.get('number_commit')
                to_blog_id = request.POST.get('to_blog_id')
                blog_commit = request.POST.get('blog_commit')
                # print(blog_commit)
                item = {
                    "number_commit": number_commit,
                    "to_blog_id": to_blog_id,
                    "blog_commit": blog_commit
                }
                print(item)
                blog_detail = get_object_or_404(Blog, pk=to_blog_id)
                comments = Comment.objects.get(number_commit=number_commit)
                # print(number_commit)
                # print(to_blog_id)
                # print(blog_commit)
                if blog_commit:
                    Comment.objects.create(to_blog_id=blog_detail, blog_commit=blog_commit, from_id=comments,
                                           user_name=username)
                    return HttpResponse(json.dumps("回复成功"))

                else:
                    return HttpResponse(json.dumps("输入不能空"))
            else:
                return HttpResponse(json.dumps("请重试..."))
        else:
            return HttpResponse(json.dumps("请登录后再评论！！！"))
    pass