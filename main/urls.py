from django.urls import path
from . import views


app_name = "main"

#Defición de enlaces para conectar con las vistas
urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

	path('', views.IndexView.as_view(), name="home"),
 	path('contact/', views.TestimonialAddInfo.as_view(), name="contact"),

	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	path('blogaddinfo/', views.BlogAddInfo.as_view(), name = "blogaddinfo"),
	]

    