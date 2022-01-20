from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.contrib.auth.models import User
from blog.filters import PostFilter
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
# def home(request):
#     posts=Post.objects.all()
#     fil=PostFilter(request.GET,queryset=posts)
#     posts=fil.qs
#     context={'filter':fil,'posts':posts}
#     return render(request,'home.html',context)

class PostListView(ListView):
    model=Post
    template_name='blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        fil = PostFilter(self.request.GET,queryset=self.get_queryset())
        context['filter']=fil
        return context
    ordering=['-date']
    paginate_by=5

class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        
        return Post.objects.filter(author=user).order_by('-date')
    

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post

    success_url='/'
    
    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user:
            return True
        return False


def about(request):
    return render(request,'about.html',{'title':'about'})