from django import forms
from tinymce import TinyMCE
from . models import Post, Comment
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class TinyMCEWidget(TinyMCE):
	def use_required_attribute(self, *args):
		return False

class PostForm(forms.ModelForm):
	content = forms.CharField(
		widget=TinyMCEWidget(
			attrs={'required': False, 'cols': 30, 'rows': 10}
		)
	)

class Meta:
	model = Post
	fields = '__all__'


class CommentForm(forms.ModelForm):

	name = forms.CharField(label='', widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Type your name',
		'id': 'username',

		}))

	comment = forms.CharField(label='', widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Type your comment ',
		'id': 'usercomment',
		'rows': 5,

		}))

	captcha = ReCaptchaField(label='', widget=ReCaptchaV2Checkbox(attrs={
			'class': 'post-captcha',
            'data-theme': 'light',
        }))

	class Meta:
		model = Comment
		fields = ('name', 'comment', )

