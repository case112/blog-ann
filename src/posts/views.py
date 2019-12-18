from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . models import Post
from .forms import CommentForm
from django.views.generic.base import TemplateView
from django.contrib import messages


class InstaView(TemplateView):

    template_name = "insta.html"
    extra_context={
        "instagram_profile_name": "anngretts"
    }



def index(request):
	featured = Post.objects.filter(status=1, featured=True)
	latest = Post.objects.filter(status=1).order_by('-created_on')[0:3]
	context = {
		'object_list': featured,
		'latest': latest,
		'instagram_profile_name': 'anngretts',
	}
	return render(request, 'index.html', context)

def contact(request):
	return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})


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
			form.instance.post = post
			form.save()
			messages.success(request, 'Comment submited, thank you! It will appear after moderation.')

	return render(request, 'post.html', {
		'post': post, 
		'next_post': next_post,
		'previous_post': previous_post,
		'form': form,
		})



