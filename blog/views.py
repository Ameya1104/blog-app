from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, AddCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get("post_id"))
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse("post_detail", args=[str(pk)]))

def DisLikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get("post_id"))
	post.dislikes.add(request.user)
	return HttpResponseRedirect(reverse("post_detail", args=[str(pk)]))	

class IndexView(ListView):
	model = Post
	template_name = 'index.html'
	ordering = ['-created_on']
	success_message = 'List successfully saved!!!!'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, "category_list.html", {'cat_menu_list':cat_menu_list})	

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category = cats.title().replace('-',' '))
	return render(request, "category.html", {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})	

class PostDetailView(DetailView):
	model = Post
	template_name = 'post_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(PostDetailView, self).get_context_data(*args, **kwargs)

		stuff = get_object_or_404(Post, id =self.kwargs['pk'])
		total_likes = stuff.total_likes()
		total_dislikes = stuff.total_dislikes()
		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["total_dislikes"] = total_dislikes
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddPostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

# Add Comment View
class AddCommentView(CreateView):
	model = Comment
	form_class = AddCommentForm
	template_name = 'add_comment.html'
	success_url = reverse_lazy("index")

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class EditPostView(UpdateView):
	model = Post
	template_name = 'update_post.html'
	fields = ['title', 'body']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(EditPostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('index')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(DeletePostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

