from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView, ListView
from press.models import Post, PostStatus, Category, CoolUser


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts_detail.html', {'post_obj': post})


def post_list(request):
    posts_list = Post.objects.filter(status=PostStatus.PUBLISHED.value).order_by('-pk')[:20]
    return render(request, 'posts_list.html', {'post_list': posts_list})


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'categories_detail.html', {'category_obj': category})


def category_list(request):
    categories_list = Category.objects.order_by('-pk')[:20]
    return render(request, 'categories_list.html', {'category_list': categories_list})


class CategoryDetail(DetailView):
    model = Category


class CategoryList(ListView):
    model = Category


class PostListView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'posts_list.html'


class PostListByCoolUser(PostListView):
    def get_queryset(self):
        queryset = super(PostListByCoolUser, self).get_queryset()
        cool_user_id = self.kwargs['cool_user_id']
        cool_user = get_object_or_404(CoolUser, id=cool_user_id)
        return queryset.filter(author=cool_user)
