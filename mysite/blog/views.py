from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Post
from .models import Blog


def post_list(request):
    posts = Post.objects.all()
    blogs = Blog.objects
    return render(request, 'blog/post_list.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})


def base(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    return render(request, 'blog/base.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})
