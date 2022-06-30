
from django.urls import path
from .views import UploadFeed, Profile, UploadReply, ToggleLike,ToggleBookmark, gallery, gift, realgift, realgift2



urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('like', ToggleLike.as_view()),
    path('reply', UploadReply.as_view()),
    path('bookmark', ToggleBookmark.as_view()),
    path('profile', Profile.as_view()),
    path('gallery', gallery.as_view()),
    path('gift', gift.as_view()),
    path('realgift', realgift.as_view()),
    path('realgift2', realgift2.as_view()),

    ]




