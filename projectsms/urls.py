from django.contrib import admin
from django.urls import path
from projectsms import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from accounts.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landingPage, name='landing'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('product_details/<slug>', views.product_details, name='product_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
