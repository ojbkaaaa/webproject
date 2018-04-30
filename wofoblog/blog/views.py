from django.shortcuts import render,get_object_or_404,redirect,render_to_response
from django.http import HttpResponse
from utils import pagination
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from .models import User_info, Tag, Blog
from comments.models import Comment
from .forms import User_infoForm ,LoginFrom
import json, os
# Create your views here.



def index(request):# 首页
    # blog_list = Blog.objects.all().order_by('-create_data')
    # print(blog_list)
    username = request.session.get('username')
    return render(request, 'blog/index.html', {'username': username})
    pass
@csrf_exempt
def login(request):
    if request.method == "POST":
        uf = User_infoForm(request.POST)
        lg = LoginFrom(request.POST)
        # print(uf)
        info ={'status': None, 'error_lg': '', 'error_f': '', 'data': None}
        if lg.is_valid():
            f = User_infoForm()
            username = lg.cleaned_data['username']
            pwd = lg.cleaned_data['password']
            # print(username +':'+pwd )
            udb = User_info.objects.filter(name=username)
            pwb = User_info.objects.filter(name=username, pwd=pwd)
            # print(udb+':'+pdb)
            if udb:
                if pwb:
                    request.session['username'] = username
                    print(username)
                    print(pwd)
                    print(udb)
                    print('1')
                    #return redirect('/blog/index/')
                    return redirect('/blog/index/')
                else:
                    print('2')
                    info['error_lg'] = "密码错误"
            else:
                print('3')
                info['error_lg'] = "用户名不存在"
            print(info)
            return render(request, "blog/login.html", {"uf": f, 'lg': lg, 'info': info})

        if uf.is_valid():
            lg = LoginFrom()
            username = uf.cleaned_data["name"]
            pwd = uf.cleaned_data["pwd"]
            email = uf.cleaned_data["email"]
            phone = uf.cleaned_data["phone"]
            common = uf.cleaned_data["common"]
            try:
                User_info.objects.get(name=username)
                info['status'] = True
                info['error_f'] = "创建失败,已存在相同用户"

            except:
                User_info.objects.create(name=username, pwd=pwd, email=email, phone=phone, common=common)
                info['error_f'] = "创建成功，点击login登录"
                info['status'] = True
            return render(request, "blog/login.html", {"uf": uf, 'lg': lg, 'info': info})
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        f = User_infoForm()
        l = LoginFrom()
        # print(f.as_p())
        print(l)
        c = csrf(request)
        c.update({"uf": f, "lg": l})
        return render_to_response( "blog/login.html", context=c)

# def register(request):
#     f = User_infoForm()
#     l = LoginFrom()
#     if request.method == "POST":
#         info = {'status': True, 'error': None, 'data': None}
#         f = User_infoForm(request.POST)
#         print('register')
#         print(f)
#         if f.is_valid():
#             username = f.cleaned_data["name"]
#             pwd = f.cleaned_data["pwd"]
#             email = f.cleaned_data["email"]
#             phone = f.cleaned_data["phone"]
#             common = f.cleaned_data["common"]
#             try:
#                 User_info.objects.get(name=username)
#                 info['status'] = False
#                 info['error'] = "创建失败,已存在相同用户"
#             except:
#                 User_info.objects.create(name=username, pwd=pwd, email=email, phone=phone, common=common)
#                 info['error'] = "创建成功，点击login登录"
#             return render(request, "blog/login.html", {"uf": f, 'lg':l, 'info': info})
#             # try:
#             #     User_info.objects.get(name=username)
#             # except:
#             #     User_info.objects.create(name=username, pwd=pwd, email=email, phone=phone, common=common)
#             #     return redirect('blog/login')
#             # info['status'] = False
#             # info['error'] = "创建失败,已存在相同用户"
#             # return render(request, "blog/login.html", {'info': info, "uf": f})
#         else:
#             print('222')
#             print(f.errors)
#             return render(request, "blog/login.html", {"uf": f})






# def login(request):
#     if request.method == "POST":
#         lg = LoginFrom(request.POST)
#         # print(uf)
#         info ={'status': True, 'error': None, 'data': None}
#         if lg.is_valid():
#             username = lg.cleaned_data['username']
#             pwd = lg.cleaned_data['password']
#             # print(username +':'+pwd )
#             udb = User_info.objects.filter(name=username)
#             pwb = User_info.objects.filter(name=username, pwd=pwd)
#             # print(udb+':'+pdb)
#             if udb:
#                 if pwb:
#                     request.session['username'] = username
#                     print(username)
#                     print(pwd)
#                     print(udb)
#                     print('1')
#                     #return redirect('/blog/index/')
#                     info['error'] = "/blog/index/"
#                 else:
#                     print('2')
#                     info['status'] = False
#                     info['error'] = "密码错误"
#             else:
#                 print('3')
#                 info['status'] = False
#                 info['error'] = "用户名不存在"
#             print(info)
#             return HttpResponse(json.dumps(info))
#         else:
#             error = lg.errors
#             c = csrf(request)
#             c.update({"error": error, "lg": lg})
#             return render_to_response("blog/login.html", context=c)
#     else:
#         # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
#         f = User_infoForm()
#         l = LoginFrom()
#         # print(f.as_p())
#         print(l)
#         c = csrf(request)
#         c.update({"uf": f, "lg": l})
#         return render_to_response( "blog/login.html", context=c)
# # def login(request):# 登录验证
# #     print('11')
# #     if request.method == 'POST':
# #         print('44')
# #         uf = forms.User_infoForm(request.POST)
# #         info = {'uf': uf, 'error': '', 'flag': ''}
# #
# #         # print(uf)
# #         if uf.is_valid():
# #             username = uf.cleaned_data['name']
# #             pwd = uf.cleaned_data['pwd']
# #             # print(username +':'+pwd )
# #             udb = User_info.objects.filter(name=username, pwd=pwd)
# #
# #             # print(udb+':'+pdb)
# #             if udb:
# #                 request.session['username'] = username
# #                 return redirect('/blog/index')
# #             else:
# #                 print('22')
# #                 return redirect('blog/login')
# #         else:
# #             print(uf.errors)
# #             info['error'] = uf.errors
# #             info['flag'] = '103'
# #             print('55')
# #             return render(request, 'blog/login.html', {'uf': uf})
# #     else:
# #         uf = forms.User_infoForm()
# #         print('33')
# #         return render(request, 'blog/login.html', {'uf': uf})
#
# def register(request):
#     f = User_infoForm()
#     l = LoginFrom()
#     if request.method == "POST":
#         info = {'status': True, 'error': None, 'data': None}
#         f = User_infoForm(request.POST)
#         print('register')
#         print(f)
#         if f.is_valid():
#             username = f.cleaned_data["name"]
#             pwd = f.cleaned_data["pwd"]
#             email = f.cleaned_data["email"]
#             phone = f.cleaned_data["phone"]
#             common = f.cleaned_data["common"]
#             try:
#                 User_info.objects.get(name=username)
#                 info['status'] = False
#                 info['error'] = "创建失败,已存在相同用户"
#             except:
#                 User_info.objects.create(name=username, pwd=pwd, email=email, phone=phone, common=common)
#                 info['error'] = "创建成功，点击login登录"
#             return render(request, "blog/login.html", {"uf": f, 'lg':l, 'info': info})
#             # try:
#             #     User_info.objects.get(name=username)
#             # except:
#             #     User_info.objects.create(name=username, pwd=pwd, email=email, phone=phone, common=common)
#             #     return redirect('blog/login')
#             # info['status'] = False
#             # info['error'] = "创建失败,已存在相同用户"
#             # return render(request, "blog/login.html", {'info': info, "uf": f})
#         else:
#             print('222')
#             print(f.errors)
#             return render(request, "blog/login.html", {"uf": f})


def out(request):
    request.session.clear()
    username = request.session.get('username')
    return render(request, 'blog/index.html', {'username': username})

def check_login(func, **kwargs):
    def inner(request):
        try:
            session = request.session.get('username')
            if session:
                # print(session)
                return func(request)
            else:
                return redirect('/blog/login')
        except:
            pass
    return inner

def put(request):  #  新增博客
    username = request.session.get('username')
    if request.method == 'POST':
        session = request.session.get('username')
        info_title = request.POST.get('title')
        info_tag = request.POST.get('blog_tag')
        info_content = request.POST.get('blog_content')
        # info_image = request.POST.get('blog_image')
        try:
            Tag.objects.get(tag_name=info_tag)
        except:
            Tag.objects.create(tag_name=info_tag)
            info_tag = Tag.objects.get(tag_name=info_tag)
        finally:
            user = User_info.objects.get(name=session)
            tt = Blog.objects.create(title=info_title, blog_tag=Tag.objects.get(tag_name=info_tag),
                                     blog_content=info_content)
            # blog.author.set(user)
            # blog.save()
            user.blog_set.add(tt)
        return render(request, 'blog/put.html', {'username': username})

    else:
        return render(request, 'blog/index.html', {'username': username})

def commit(request):# 评论
    pass

def detail(request,pk):# 博文详细
    username = request.session.get('username')
    blog_detail = get_object_or_404(Blog, pk=pk)
    blog_detail.add_views()  # 阅读量+1
    # blog_detail.views += 1
    # blog_detail.save()
    # print(blog_detail)
    nodes = blog_detail.comment_set.all()
    details = Blog.objects.all().get(title=blog_detail, blog_number=pk)
    # details.add_views()
    # details.increase_views()
    # print(details)
    return render(request, 'blog/detail.html', {"context": details, 'username': username, 'nodes': nodes})
    pass

def blog(request): # 所有博客
    username = request.session.get('username')
    wd = request.GET.get('wd')  # 搜索框

    # blog_set = Blog.objects.all().order_by('-create_data')
    current_page = request.GET.get("p", 1)
    current_page = int(current_page)
    # val = request.COOKIES.get('per_page_count') # 获取每页显示的个数
    val = 9
    li = Blog.objects.all().count()
    page_obj = pagination.Page(current_page, int(li), val)
    if wd:
        data = Blog.objects.filter(title__icontains=wd).order_by('-views')[page_obj.start:page_obj.end]
    else:
        data = Blog.objects.all().order_by('-views')[page_obj.start:page_obj.end]



    page_str = page_obj.page_str("/blog/blog/")
    tag_list = Tag.objects.all()[:7]
    return render(request, "blog/blog.html", {"blog_set": data, "page_str": page_str, 'tag_list': tag_list,
                                              'username': username})
   #  return render(request, 'blog/blog.html', {'blog_set': blog_set})

# def find(request):
#     username = request.session.get('username')
#     # blog_set = Blog.objects.all().order_by('-create_data')
#     current_page = request.GET.get("p", 1)
#     current_page = int(current_page)
#     # val = request.COOKIES.get('per_page_count') # 获取每页显示的个数
#     val = 9
#     li = Blog.objects.all().count()
#     page_obj = pagination.Page(current_page, int(li), val)
#     find_some = request.GET.get('wd')
#     print(find_some)
#     data = Blog.objects.filter(title=find_some).order_by('views')[page_obj.start:page_obj.end]
#     page_str = page_obj.page_str("/blog/blog/")
#     tag_list = Tag.objects.all()[:7]
#     return render(request, "blog/blog.html",
#                   {"blog_set": data, "page_str": page_str, 'tag_list': tag_list, 'username': username})
#     pass

def contact(request):
    username = request.session.get('username')
    if username:
        return render(request, 'blog/self.html')
    else:
        return redirect( '/blog/login')

def user_info(request):# 后台管理
    username = request.session.get('username')
    # print(username)
    if username:
        # 利用多对多操作实现只显示该用户的博客
        number = User_info.objects.get(name=username)
        # print(number)
        blog_list = number.blog_set.all()
        name_info = get_object_or_404(User_info, name=username)
        # print(name_info)
        name = name_info.name
        pwd = name_info.pwd
        email = name_info.email
        phone = name_info.phone
        common = name_info.common
        headImg = name_info.headImg
        # print(phone)
        # print(blog_list)
        # for i in blog_list:
        #     print(i.author)
        if request.method == 'POST':
            if request.is_ajax:  # 通过ajax新增（还需优化）
                title = request.POST.get('title')
                blog_tag = request.POST.get('blog_tag')
                blog_content = request.POST.get('blog_content')
                session = request.session.get('username')
                info_title = request.POST.get('title')
                info_tag = request.POST.get('blog_tag')
                info_content = request.POST.get('blog_content')
                # info_image = request.POST.get('blog_image')
                try:
                    Tag.objects.get(tag_name=info_tag)
                except:
                    Tag.objects.create(tag_name=info_tag)
                    info_tag = Tag.objects.get(tag_name=info_tag)
                finally:
                    user = User_info.objects.get(name=session)
                    tt = Blog.objects.create(title=info_title, blog_tag=Tag.objects.get(tag_name=info_tag),
                                             blog_content=info_content
                                             )
                    # blog_detail = get_object_or_404(Blog, pk=tt.blog_number)
                    # blog_detail.add_blog_excerpt
                    # print(blog_detail.blog_excerpt)
                    # blog.author.set(user)
                    # blog.save()
                    user.blog_set.add(tt)
            c = csrf(request)
            c.update({'blog_list': blog_list, 'name': name, 'email': email, 'phone': phone, 'common': common, 'headImg':headImg,'pwd': pwd,
                      'username': username})
            return render_to_response('blog/user_info.html', context=c)
        else:
            c = csrf(request)
            c.update({'blog_list': blog_list, 'name': name, 'email': email, 'phone': phone, 'common': common, 'headImg':headImg,'pwd': pwd,
                      'username': username})
            return render_to_response('blog/user_info.html', context=c)
    else:
        uf = User_infoForm()
        l = LoginFrom()
        return render(request, 'blog/login.html', {'uf': uf, "lg": l})


def user_page(request):
    username = request.session.get('username')
    current_page = request.GET.get("p", 1)
    current_page = int(current_page)
    # val = request.COOKIES.get('per_page_count') # 获取每页显示的个数
    val = 9
    li = Blog.objects.all().count()
    page_obj = pagination.Page(current_page, int(li),val)
    data = Blog.objects.all()[page_obj.start:page_obj.end]
    page_str = page_obj.page_str("/app3/user_page/")
    return render(request, "user_list.html", {"data": data, "page_str": page_str, 'username': username})

def add(request):
    if request.is_ajax:
        print(request.body)
        print(request.POST)
        # print(request.GET)
        title = request.POST.get('title')
        blog_tag = request.POST.get('blog_tag')
        blog_content = request.POST.get('blog_content')
        print(title, blog_tag, blog_content)
        res = {"msg": 'true'}
    else:
        res = {"msg": 'error'}
    return HttpResponse(json.dumps(res))
    pass

# def image(request):
#     print(request.POST)
#     file_obj = request.FILES.get('avatar')
#     # print(file_obj)
#     file_path = os.path.join('media/img', file_obj.name)
#     with open(file_path, 'wb') as f:
#         for chunk in file_obj.chunks():
#             f.write(chunk)
#     # print(file_obj)
#     return HttpResponse(file_path)
#
#     pass
def imageupdate(request):
    username = request.session.get('username')
    # base_dic = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # base_dic = os.path.join(base_dic, 'media')
    # print(base_dic)
    if username:
        # print('1111')
        # 利用多对多操作实现只显示该用户的博客
        # number = User_info.objects.get(name=username)
        # print(number)
        # print(name_info)
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        common = request.POST.get('common')
        base_dic = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(base_dic)
        uf = User_infoForm(request.POST)
        # print(uf.errors)
        base_dic = os.path.join(base_dic, 'media\headImg')
        # print(base_dic)
        file_obj = request.FILES.get('avatar')
                try:
            base_dic = os.path.join(base_dic, file_obj.name)
            # print('3')
        except:
            # print('4')
            base_dic = os.path.join(base_dic, 'uiface2.png')
        if file_obj:
            with open(base_dic, 'wb') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
            User_info.objects.filter(name=username).update(name=username, email=email, phone=phone, common=common,
                                                           pwd=pwd,
                                                           headImg=file_obj)
        else:
            User_info.objects.filter(name=username).update(name=username, email=email, phone=phone, common=common,
                                                           pwd=pwd)

        return HttpResponse(base_dic)


    pass

def tagview(request,pk):
    username = request.session.get('username')
    current_page = request.GET.get("p", 1)
    current_page = int(current_page)
    # val = request.COOKIES.get('per_page_count') # 获取每页显示的个数
    val = 9
    li = Blog.objects.all().count()
    page_obj = pagination.Page(current_page, int(li), val)
    tag = Blog.objects.filter(blog_tag=pk).order_by('-views')[page_obj.start:page_obj.end]
    page_str = page_obj.page_str("/blog/blog/")
    tag_list = Tag.objects.all()[:7]
    return render(request, "blog/blog.html", {"blog_set": tag, "page_str": page_str, 'tag_list': tag_list,
                                              'username': username})

    pass


@csrf_exempt
def page_not_found(request):
    print(request.POST)
    print(request.GET)
    return render_to_response('blog/404.html')

@csrf_exempt
def page_error(request):
    print(request.POST)
    print(request.GET)
    return render_to_response('blog/500.html')
