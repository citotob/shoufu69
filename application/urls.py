#from django.conf.urls import include, url
from django.urls import include, path
from django.contrib import admin
from jet.dashboard.dashboard_modules import google_analytics_views

admin.autodiscover()

urlpatterns = [
    #path('videos/', include('videos.urls', 'videos')),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    #url(r'^admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),
]
