from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

User = get_user_model()


class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_picture = models.ImageField()

	def __str__(self):
		return self.user.username

class Category(models.Model):
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=200, unique=True, default="")
	overview = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	content = HTMLField(default="")
	comment_count = models.IntegerField(default=0)
	view_count = models.IntegerField(default=0)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	thumbnail = models.ImageField()
	categories = models.ManyToManyField(Category)
	featured = models.BooleanField()
	status = models.IntegerField(choices=STATUS, default=0)
	


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={
			'slug': self.slug
		})

	@property
	def get_comments(self):
		return self.comments.all().order_by('-created_date')
	

	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=200)
	comment = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.comment





