from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from .utils import *

# Create your views here.


class GamesHome(DataMixin, ListView):
    model = Games
    template_name = 'games/index.html'
    context_object_name = 'posts' # переменная в шаблоне индекс

    #Добавление меню

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главна страница')
        return context | c_def #dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Games.objects.filter(is_published=True)




# def about(request):
#     return render(request, 'games/about.html')


class About(DataMixin, TemplateView):
    template_name = 'games/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О нас')
        return context | c_def


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'games/add_page.html'
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return context | c_def  #dict(list(context.items()) + list(c_def.items()))


#def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления статьи')
#     else:
#         form = AddPostForm()
#     return render(request, 'games/add_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


# def contact(request):
#     return render(request, 'games/contact.html')


# def login(request):
#     return render(request, 'games/login.html')


def register(request):
    return render(request, 'games/login.html')


class Games_show_catogory(DataMixin, ListView):
    model = Games
    template_name = 'games/index.html'
    context_object_name = 'posts'
    allow_empty = False  # if posts out of range = 404

    def get_queryset(self):
        return Games.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория' + ' ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return context | c_def
# def show_category(request, cat_slug):
#     cats = Category.objects.all()
#     posts = Games.objects.filter(cat__slug=cat_slug)
#     context = {
#         'posts': posts,
#         'title': 'Все категории',
#         'cat_selected': cat_slug,
#     }
#     return render(request, 'games/index.html', context=context)


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')


class ShowPost(DataMixin, DetailView):
    model = Games
    template_name = 'games/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


    def get_queryset(self):
        return Games.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Статьи')
        return context | c_def

# def show_post(request, post_slug):
#     post = get_object_or_404(Games, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': 'Все категории',
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'games/post.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'games/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'games/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вход')
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(requset):
    logout(requset)
    return redirect('home')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'games/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return context | c_def

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class Hide(DataMixin, TemplateView):
    template_name = 'games/hide.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Heart')
        return context | c_def