
from django import forms
from .models import Blog, ContactProfile, Testimonial

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class ContactForm(forms.ModelForm):

# 	name = forms.CharField(max_length=100, required=True,
# 		widget=forms.TextInput(attrs={
# 			'placeholder': '*Full name..',
# 			}))
# 	email = forms.EmailField(max_length=254, required=True, 
# 		widget=forms.TextInput(attrs={
# 			'placeholder': '*Email..',
# 			}))
# 	message = forms.CharField(max_length=1000, required=True, 
# 		widget=forms.Textarea(attrs={
# 			'placeholder': '*Message..',
# 			'rows': 6,
# 			}))


# 	class Meta:
# 		model = ContactProfile
# 		fields = ('name', 'email', 'message',)

#Define los datos (con nombre y tipo) a llenar de las clases

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class BlogForm(forms.ModelForm):
	author = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder':'Autor...',
		}))
	name = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder':'Nombre del Manga...',
		}))
	description = forms.CharField(max_length=500, required=True,
		widget=forms.TextInput(attrs={
			'placeholder':'Descripción...',
		}))

	image = forms.ImageField()

	body = forms.CharField(max_length=2000, required=True,
		widget=forms.TextInput(attrs={
			'placeholder':'Info del Manga...',
		}))

	class Meta: 
		model = Blog
		fields =['author', 'name', 'description', 'body', 'image']

class TestimonialForm(forms.ModelForm):

	thumbnail = forms.ImageField()
	name = forms.CharField(max_length=200, required=True,
			widget=forms.TextInput(attrs={
				'placeholder':'Autor...',
			}))
	
	quote = forms.CharField(max_length=500, required=True,
			widget=forms.TextInput(attrs={
				'placeholder':'Comentario...',
			}))	
  
	class Meta: 
		model = Testimonial
		fields =['thumbnail', 'name', 'quote']