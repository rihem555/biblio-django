from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from livres import views as livres_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('livres.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='livres/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', livres_views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
