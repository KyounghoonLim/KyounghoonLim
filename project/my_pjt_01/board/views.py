from django import forms
from django.core import paginator
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.shortcuts import get_object_or_404, redirect, render
from .models import Board
from .forms import BoardForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    articles = Board.objects.order_by('-pk')
    paginator = Paginator(articles, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    num1 = len(Board.objects.filter(header='1'))
    num2 = len(Board.objects.filter(header='2'))
    

    context = {
        'articles': page_obj,
        'free': num1,
        'repeat': num2,
    }
    return render(request, 'board/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('board:index')
    else:
        form = BoardForm()
    context = {
        'form': form
    }
    return render(request, 'board/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Board, pk)
    context = {
        'article': article,
    }
    return render(request, 'board/detail.html', context)