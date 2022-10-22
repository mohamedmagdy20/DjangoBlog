from urllib import response
from django.views.generic import ListView , DetailView, CreateView , DeleteView , UpdateView 
from django.shortcuts import render
from .models import Post
from comments.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.http import JsonResponse
posts = Post.objects.all()

def home(request):
    # commentCount = Comment.objects.filter
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'blog'})

class PostListView(ListView):
    model = Post
    template_name: str = 'blog/home.html'
    context_object_name= 'posts'  
    # ordering: ["-date_posted"]  

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    fields= ['title','content']
    def form_valid(self,form):   
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields= ['title','content']
    def form_valid(self,form):   
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False   

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False   

def addStar(request):
    if request.method == 'POST':
        # return request.POST.get('id')
        post  =Post.objects.get(pk=request.POST.get('id'))
        starCount = post.stars
        starCount += 1
        post.stars = starCount
        post.save()
        return JsonResponse({'message':'success'})
