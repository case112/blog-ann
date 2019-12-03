from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from . models import Post

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

def post(request, id):
	post = get_object_or_404(Post, id=id)
	context = {
		'post': post,
	}
	return render(request, 'post.html', context)
