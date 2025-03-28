from django.urls import path
from .views import crud

urlpatterns = [
    # User URLs
    path('user/', crud.UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', crud.UserDetailView.as_view(), name='user_detail'),
    path('user/create/', crud.UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>/update/', crud.UserUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', crud.UserDeleteView.as_view(), name='user_delete'),

    # Image URLs
    path('image/', crud.ImageListView.as_view(), name='image_list'),
    path('image/<int:pk>/', crud.ImageDetailView.as_view(), name='image_detail'),
    path('image/create/', crud.ImageCreateView.as_view(), name='image_create'),
    path('image/<int:pk>/update/', crud.ImageUpdateView.as_view(), name='image_update'),
    path('image/<int:pk>/delete/', crud.ImageDeleteView.as_view(), name='image_delete'),

    # ImageCollection URLs
    path('imagecollection/', crud.ImageCollectionListView.as_view(), name='imagecollection_list'),
    path('imagecollection/<int:pk>/', crud.ImageCollectionDetailView.as_view(), name='imagecollection_detail'),
    path('imagecollection/create/', crud.ImageCollectionCreateView.as_view(), name='imagecollection_create'),
    path('imagecollection/<int:pk>/update/', crud.ImageCollectionUpdateView.as_view(), name='imagecollection_update'),
    path('imagecollection/<int:pk>/delete/', crud.ImageCollectionDeleteView.as_view(), name='imagecollection_delete'),

    # GhibliStyle URLs
    path('ghiblistyle/', crud.GhibliStyleListView.as_view(), name='ghiblistyle_list'),
    path('ghiblistyle/<int:pk>/', crud.GhibliStyleDetailView.as_view(), name='ghiblistyle_detail'),
    path('ghiblistyle/create/', crud.GhibliStyleCreateView.as_view(), name='ghiblistyle_create'),
    path('ghiblistyle/<int:pk>/update/', crud.GhibliStyleUpdateView.as_view(), name='ghiblistyle_update'),
    path('ghiblistyle/<int:pk>/delete/', crud.GhibliStyleDeleteView.as_view(), name='ghiblistyle_delete'),

    # StyledImageJob URLs
    path('styledimagejob/', crud.StyledImageJobListView.as_view(), name='styledimagejob_list'),
    path('styledimagejob/<int:pk>/', crud.StyledImageJobDetailView.as_view(), name='styledimagejob_detail'),
    path('styledimagejob/create/', crud.StyledImageJobCreateView.as_view(), name='styledimagejob_create'),
    path('styledimagejob/<int:pk>/update/', crud.StyledImageJobUpdateView.as_view(), name='styledimagejob_update'),
    path('styledimagejob/<int:pk>/delete/', crud.StyledImageJobDeleteView.as_view(), name='styledimagejob_delete'),

]