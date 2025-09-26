from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from unicodedata import category
from django.http import HttpResponse
from .forms import *
from .models import Post
from django.views.generic import ListView
from django.views.generic import FormView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# def indexview(request):
#     name="Ali"
#     context = {"name":name}
#     return render(request,'index.html',context)

# CBV for pages
class Indexview(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Ali"
        context["posts"] = Post.objects.all()
        return context

#class for redirecting
class RedirectToMaktab(RedirectView):
    permanent = True
    url = 'https://maktabkhooneh.org/'


class PostList(ListView):
    paginate_by = 2
    ordering = 'id'
    model = Post
    context_object_name = 'posts'

'''
class Postcreateview(FormView):
    form_class = Postform
    template_name = 'blog/contact.html'
    success_url = '/blog/go to maktab/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''
class Postcreateview(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['author', 'title', 'content','status','category']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
@api_view(['GET', 'POST'])
def APIPostcreate(request):
    return Response('OK')