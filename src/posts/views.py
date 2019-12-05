from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from . models import Post
from .forms import CommentForm


def index(request):
	featured = Post.objects.filter(status=1, featured=True)
	latest = Post.objects.filter(status=1).order_by('-created_on')[0:3]
	context = {
		'object_list': featured,
		'latest': latest,
	}
	return render(request, 'index.html', context)

def blog(request):
	post_list = Post.objects.filter(status=1)
	most_recent = Post.objects.filter(status=1).order_by('-created_on')[0:3]
	paginator = Paginator(post_list, 6)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)
	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)

	context = {
		'queryset': paginated_queryset,
		'most_recent': most_recent,
		'page_request_var': page_request_var,
	}
	return render(request, 'blog.html', context)

def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	try:
		next_post = post.get_next_by_created_on()
	except Post.DoesNotExist:
		next_post = None
	try:
		previous_post = post.get_previous_by_created_on()
	except Post.DoesNotExist:
		previous_post = None


	form = CommentForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()

	return render(request, 'post.html', {
		'form': form,
		'post': post, 
		'next_post': next_post,
		'previous_post': previous_post,
		})



