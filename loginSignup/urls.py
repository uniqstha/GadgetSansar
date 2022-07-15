from django.urls import path,include
from loginSignup import views
urlpatterns = [
    # path('admin/', admin.site.urls),

    # path('',views.index),
    path('loginsignup',views.login_signup),
    path('profile',views.profile),
    path('logout',views.logout_fn)
  
 
    
]