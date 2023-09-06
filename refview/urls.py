from django.urls import path

from . import views

urlpatterns = [
        path('', views.Index.as_view(), name="index"),
        #path('upload', views.upload, name="upload"),
        path("upload", views.UploadView.as_view(), name="upload"),
        path('<int:pk>/',
             views.ImageDetailView.as_view(),
             name="detail"
         ),
        path('random', views.RandomImageView.as_view(), name="random")
]
