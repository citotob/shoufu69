#from django.conf.urls import include, url
from django.urls import include, path
from django.contrib import admin
from jet.dashboard.dashboard_modules import google_analytics_views
from django.conf import settings
from django.conf.urls.static import static
from defang import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth import views as auth_views
from accounts.views import logout, SignUp, UpdateProfile, profile

admin.autodiscover()

urlpatterns = [
    #path('videos/', include('videos.urls', 'videos')),
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    #url(r'^admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),

    path('signin/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='signin'),
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', logout, name="logout"),
    path('profile/edit/', profile, name="profile"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'
         ),
         name='password_reset_complete'),

#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
# Add media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)