from django.shortcuts import render,redirect
from blog.models import Post
from comments.forms import CommentForm
from django.contrib import messages
from comments.models import Comment

# Create your views here.
def showComments(request,id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post = id)
    comment_count = comments.count()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment =  form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request,'Comment Saved') 
            return redirect('showcomments',id)          
    else:
        form = CommentForm()
    return render(request,'comments/comments.html',{'comments':comments,'post':post,'form':form,'comment_count':comment_count})

# def addComment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Comment Saved') 
#             return redirect('blog_home')          
#     else:
#         form = CommentForm()
#     return form    

def deleteComment(request,id):
    comment = Comment.objects.get(pk=id)
    post_id = comment.post.id
    comment.delete()
    messages.success(request,'Comment Deleted')
    return redirect('showcomments',post_id)