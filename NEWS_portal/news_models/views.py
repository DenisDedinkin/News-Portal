from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import *

from .filters import PostFilter
from .forms import NewsForm, ArticlesForm
from .models import Post, Category


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    return redirect('home')


@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)
    return redirect('home')


class NewsList(ListView):
    model = Post  # Указываем модель, объекты которой мы будем выводить
    ordering = 'time_in'  # Поле, которое будет использоваться для сортировки объектов
    template_name = 'news.html'  # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    context_object_name = 'news'  # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 10  # количество записей на странице

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post  # Модель всё та же, но мы хотим получать информацию по отдельному посту
    template_name = 'post.html'  # Используем другой шаблон — post.html
    context_object_name = 'post'  # Название объекта, в котором будет выбранный пользователем продукт


class NewsCreate(PermissionRequiredMixin, CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')
    permission_required = ('news_models.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'N'
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'
    permission_required = ('news_models.change_post',)


class NewsDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
    permission_required = ('news_models.delete_post',)


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'articles_edit.html'
    permission_required = ('news_models.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'A'
        return super().form_valid(form)


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'articles_edit.html'
    permission_required = ('news_models.change_post',)


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('news_list')
    permission_required = ('news_models.delete_post',)
