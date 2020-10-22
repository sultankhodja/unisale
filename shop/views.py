from django.views import generic  # imports generic views
from .models import Post, Tag  # from models import Post table
from .forms import PostForm, SupportForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.


class IndexList(generic.ListView):  # class IndexList
    """Class to work with model as a list for rendering."""
    model = Post  # model is Post
    template_name = 'shop/index.html'  # template is index.html
    context_object_name = 'walls'  # context name is walls


class DetailView(generic.DetailView):  # class DetailView
    """Class to work with model"""
    model = Post  # model is Post
    template_name = 'shop/detail.html'  # template is detail.html


class UseView(generic.CreateView):
    """Class to work with User and Model"""
    template_name = 'shop/create.html'
    form_class = PostForm
    success_url = '/'


class SupportView(generic.CreateView):
    """Class to work with User and Model"""
    template_name = 'shop/support.html'
    form_class = SupportForm
    success_url = '/shop/index/'


class CategoriesList(generic.ListView):  # class CategoriesList
    """Class to work with model"""
    model = Tag  # model is Post
    template_name = 'shop/categories.html'  # template is categories.html
    context_object_name = 'categories'

# DetailView executes only one data, but it needs only one argument in order to execute from model (PK, SLUG).
# ListView executes all data from model without any arguments.
# Homework: CreateView

#  1.Write CBV(View classes) 2. Write a form 3.Write HTML 4.Link CBV with FORM 5.Make a path

