from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post
from .models import Blog
from blog.forms import BlogUpdate


def post_list(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'blogs': blogs, 'posts': posts})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})


def create(request):
    return render(request, 'blog/create.html')


def search(request):
    blogs = Blog.objects.all().order_by('-id')
    q = request.POST.get('q', "")
    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'blog/search.html', {'blogs': blogs, 'q': q})
    else:
        return render(request, 'blog/search.html')


def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        form = BlogUpdate(request.POST)
        if form.is_valid():
            blog.title = request.POST['title']
            blog.body = request.POST['body']
            blog.pub_date = timezone.datetime.now()
            blog.images = form.cleaned_data['images']
            blog.save()
            return redirect('/blog/detail/'+str(blog.id))
    else:
        form = BlogUpdate(instance=blog)
        return render(request, 'blog/update.html', {'form': form})


def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')


def post_create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.images = request.FILES['images']
    blog.save()
    return redirect('/blog/detail/'+str(blog.id))


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
