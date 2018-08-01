from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from datetime import datetime
from .models import Post

# 没有template版本
# def homepage(request):
#
#     posts = Post.objects.all()
#     post_lists = list()
#
#     for count, post in enumerate(posts):
#         post_lists.append("No.{}:".format(str(count)) + str(post.title) + "<br>")
#         post_lists.append("<small>" + str(post.body) + "</small><br><br>")
#     return HttpResponse(post_lists)

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals()) #渲染html,locals()函数能将内存中的变量取出,然后用字典方式打包.


    return HttpResponse(html) #在浏览器显示内容

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')