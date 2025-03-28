from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from mainapp.models import *
from django import forms

class UserListView(ListView):
    model = User
    template_name = 'mainapp/user_list.html'
    context_object_name = 'user_list'

class UserDetailView(DetailView):
    model = User
    template_name = 'mainapp/user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'password']

    template_name = 'mainapp/user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'password']

    template_name = 'mainapp/user_form.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'mainapp/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class ImageListView(ListView):
    model = Image
    template_name = 'mainapp/image_list.html'
    context_object_name = 'image_list'

class ImageDetailView(DetailView):
    model = Image
    template_name = 'mainapp/image_detail.html'
    context_object_name = 'image'

class ImageCreateView(CreateView):
    model = Image
    fields = ['user', 'original_image', 'ghibli_styled_image', 'upload_date']

    template_name = 'mainapp/image_form.html'
    success_url = reverse_lazy('image_list')

class ImageUpdateView(UpdateView):
    model = Image
    fields = ['user', 'original_image', 'ghibli_styled_image', 'upload_date']

    template_name = 'mainapp/image_form.html'
    success_url = reverse_lazy('image_list')

class ImageDeleteView(DeleteView):
    model = Image
    template_name = 'mainapp/image_confirm_delete.html'
    success_url = reverse_lazy('image_list')

class ImageCollectionListView(ListView):
    model = ImageCollection
    template_name = 'mainapp/imagecollection_list.html'
    context_object_name = 'imagecollection_list'

class ImageCollectionDetailView(DetailView):
    model = ImageCollection
    template_name = 'mainapp/imagecollection_detail.html'
    context_object_name = 'imagecollection'

class ImageCollectionCreateView(CreateView):
    model = ImageCollection
    fields = ['user', 'name', 'description', 'images', 'created_at']

    template_name = 'mainapp/imagecollection_form.html'
    success_url = reverse_lazy('imagecollection_list')

class ImageCollectionUpdateView(UpdateView):
    model = ImageCollection
    fields = ['user', 'name', 'description', 'images', 'created_at']

    template_name = 'mainapp/imagecollection_form.html'
    success_url = reverse_lazy('imagecollection_list')

class ImageCollectionDeleteView(DeleteView):
    model = ImageCollection
    template_name = 'mainapp/imagecollection_confirm_delete.html'
    success_url = reverse_lazy('imagecollection_list')

class GhibliStyleListView(ListView):
    model = GhibliStyle
    template_name = 'mainapp/ghiblistyle_list.html'
    context_object_name = 'ghiblistyle_list'

class GhibliStyleDetailView(DetailView):
    model = GhibliStyle
    template_name = 'mainapp/ghiblistyle_detail.html'
    context_object_name = 'ghiblistyle'

class GhibliStyleCreateView(CreateView):
    model = GhibliStyle
    fields = ['name', 'description']

    template_name = 'mainapp/ghiblistyle_form.html'
    success_url = reverse_lazy('ghiblistyle_list')

class GhibliStyleUpdateView(UpdateView):
    model = GhibliStyle
    fields = ['name', 'description']

    template_name = 'mainapp/ghiblistyle_form.html'
    success_url = reverse_lazy('ghiblistyle_list')

class GhibliStyleDeleteView(DeleteView):
    model = GhibliStyle
    template_name = 'mainapp/ghiblistyle_confirm_delete.html'
    success_url = reverse_lazy('ghiblistyle_list')

class StyledImageJobListView(ListView):
    model = StyledImageJob
    template_name = 'mainapp/styledimagejob_list.html'
    context_object_name = 'styledimagejob_list'

class StyledImageJobDetailView(DetailView):
    model = StyledImageJob
    template_name = 'mainapp/styledimagejob_detail.html'
    context_object_name = 'styledimagejob'

class StyledImageJobCreateView(CreateView):
    model = StyledImageJob
    fields = ['user', 'image', 'style', 'status', 'created_at', 'completed_at']

    template_name = 'mainapp/styledimagejob_form.html'
    success_url = reverse_lazy('styledimagejob_list')

class StyledImageJobUpdateView(UpdateView):
    model = StyledImageJob
    fields = ['user', 'image', 'style', 'status', 'created_at', 'completed_at']

    template_name = 'mainapp/styledimagejob_form.html'
    success_url = reverse_lazy('styledimagejob_list')

class StyledImageJobDeleteView(DeleteView):
    model = StyledImageJob
    template_name = 'mainapp/styledimagejob_confirm_delete.html'
    success_url = reverse_lazy('styledimagejob_list')
