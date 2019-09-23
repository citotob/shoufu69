#from django.conf.urls import include, url
from django.urls import include, path
from django.contrib import admin
from jet.dashboard.dashboard_modules import google_analytics_views
from django.conf import settings
from django.conf.urls.static import static
from defang import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    #path('videos/', include('videos.urls', 'videos')),
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    #url(r'^admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
# Add media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)