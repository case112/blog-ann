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
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	thumbnail = models.ImageField()
	cover_photo = models.ImageField()
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
		return self.comments.filter(approved_comment=True).order_by('created_date')
	

	
class Comment(models.Model):
	approved_comment = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=50)
	comment = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

	def approve(self):
		self.approved_comment = True
		self.save()


	def __str__(self):
		return self.comment


class Page(models.Model):
	cover_photo = models.ImageField()
	name = models.CharField(max_length=300, null=True)
	heading = models.CharField(max_length=300, null=True)
	subheading = models.CharField(max_length=300, blank=True)
	meta = models.CharField(max_length=300, blank=True)
	content = models.TextField(blank=True)


	def __str__(self):
		return self.name





