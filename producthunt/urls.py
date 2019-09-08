from django.contrib import admin
from django.urls import path, include
from products import views
import products
from accounts import views, urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    #path('accounts/login', include('accounts.urls.login')),
    #path('accounts/logout', include('accounts.urls.logout')),

]
