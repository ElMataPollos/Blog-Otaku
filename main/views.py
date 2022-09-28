from django.shortcuts import render

from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		# Portfolio,
		Testimonial,
		# Certificate
	)

from django.views import generic
# from django.views import generic
from . forms import BlogForm, CreateUserForm, TestimonialForm

#Importación de forms como el login autenticación, etc.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect

#Views se encarga de pedir y devolver los datos de la base de datos al front end
def registerPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Cuenta creada para ' + user+'!\nBienvenide!!!')

				return redirect('main:login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:home")
			else:
				messages.info(request, 'Usuario o contrseña incorrectos >:(')

		context = {}
		return render(request, 'main/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('main:login')

class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
	
		testimonials = Testimonial.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)

		context["testimonials"] = testimonials
		context["blogs"] = blogs
	
		return context


class BlogAddInfo(generic.FormView):
	template_name = "main/blogaddinfo.html"
	form_class = BlogForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Blog Creado.\nGracias por la info!!!')
		return super().form_valid(form)


class TestimonialAddInfo(generic.FormView):
	template_name = "main/contact.html"
	form_class = TestimonialForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Nos encanta tu comentario!!!! <3.')
		return super().form_valid(form)

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"