#from django.conf.urls import include, url
from django.urls import include, path
from django.contrib import admin
from jet.dashboard.dashboard_modules import google_analytics_views
from django.conf import settings
from django.conf.urls.static import static
from defang import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from albums.views import upload_picture, albums, album_photo, myalbums, album_category, album_tag
from stories.views import create_story, stories, mystories, story_page, , story_category
from videos.views import myvideos, video_page, videolikes, videodislikes, videodelete, videoedit,  video_category, video_channel, video_tag

from django.contrib.auth import views as auth_views
from accounts.views import logout, SignUp, UpdateProfile, profile

admin.autodiscover()

urlpatterns = [
    #path('videos/', include('videos.urls', 'videos')),
    path('', views.home, name='home'),
    
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
    path('password-reset-confirm/(?P<uidb64>[0-9]+)/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('upload/', views.upload, name = 'upload'),
    path('upload-video/', views.upload_video, name = 'upload-video'),
    path('upload-picture/', upload_picture, name = 'upload-picture'),

    path('create-story/', create_story, name='create-story'),
    path('stories/', stories, name='stories'),
<<<<<<< Updated upstream
    path('stories/<int:pk>/read', story_page, name='story-detail'),
    path('stories/category/<slug>', story_category, name='story-category'),
    path('mystories/', mystories, name='mystories'),

    path('albums/', albums, name='albums'),
    path('albums/<int:aid>/show', album_photo, name='album-photo'),
    path('albums/category/<slug>', album_category, name='album-category'),
    path('albums/tag/<int:pk>', album_tag, name='album-tag'),
    path('myphotos/', myalbums, name='myalbums'),
=======
    path('stories/(?P<pk>[0-9]+)/read', story_page, name='story-detail'),

    path('albums/', albums, name='albums'),
    path('albums/(?P<aid>[0-9]+)/show', album_photo, name='album-photo'),

    path('videos/(?P<pk>[0-9]+)/play', video_page, name='video-page'),
>>>>>>> Stashed changes

    path('messages/', include('django_messages.urls')),

    path('videos/<int:pk>/play', video_page, name='video-page'),
    path('myvideos/', myvideos, name='myvideos'),
    path('videos/category/<slug>', video_category, name='video-category'),
    path('videos/channel/<int:pk>', video_channel, name='video-channel'),
    path('videos/tag/<int:pk>', video_tag, name='video-tag'),

    path('videolikes/', videolikes, name='videolikes'),
    path('videodislikes/', videodislikes, name='videodislikes'),

    path('videodelete/(?P<video_id>[0-9]+)/', videodelete, name='videodelete'),
    path('edit-video/(?P<video_id>[0-9]+)/', videoedit, name='videoedit'),


#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
# Add media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)