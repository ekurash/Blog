from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse

from apps.blog.models import Post
from apps.blog.models import Tag


class ListPostView(ListView):
    model = Post
    template_name = 'post_list.html'


class CreatePostView(CreateView):
    model = Post
    fields = ('title', 'content', 'is_draft', 'tags')
    template_name = 'post_edit.html'

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:post-create')
        return context


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ('title', 'content', 'is_draft', 'tags')

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:post-edit', kwargs={'pk': self.get_object().id})
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def get_success_url(self):
        return reverse('blog:index')


class DetailPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.id})



class ListTagView(ListView):
    model = Tag
    template_name = 'tag_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:tag-create')
        return context


class CreateTagView(CreateView):
    model = Tag
    fields = ('value',)
    template_name = 'tag_edit.html'

    def get_success_url(self):
        return reverse('blog:tag-index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:tag-create')
        return context


class UpdateTagView(UpdateView):
    model = Tag
    template_name = 'tag_edit.html'
    fields = ('value', )

    def get_success_url(self):
        return reverse('blog:tag-index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse('blog:tag-edit', kwargs={'pk': self.get_object().id})
        return context


class DeleteTagView(DeleteView):
    model = Tag
    template_name = 'tag_delete.html'

    def get_success_url(self):
        return reverse('blog:tag-index')


class DetailTagView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'

    def get_absolute_url(self):
        return reverse('blog:tag-detail', kwargs={'pk': self.id})

