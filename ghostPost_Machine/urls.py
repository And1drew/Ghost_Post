from django.urls import path
from ghostPost_Machine import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('addpost/', views.addpost, name='addPost'),
    path('roastsview/', views.roastsview, name='roastsView'),
    path('boastsview/', views.boastsview, name='boastsView'),
    path('like/<int:post_id>/', views.likesview),
    path('dislike/<int:post_id>/', views.dislikesview),
    path('voteview/', views.voteview)
]
