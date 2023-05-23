from django.shortcuts import render, HttpResponse
from univeristy.models import *
from .forms import AddPostForm


def home(request):
    languages = Category.objects.all()
    return render(request, 'home.html', {"languages": languages})


def page(request, page_name):
    languages = Category.objects.all()
    category = Category.objects.get(name=page_name)
    subcategory = SubCategory.objects.filter(link=category)

    return render(
        request,
        'page.html',
        {
            'subcategories': subcategory,
            'languages': languages

        }
    )


def all(request):
    data = Category.objects.all()

    return render(request, 'all.html', {'languages': data})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                return redirect('home')
            except:
                form.add_error(None, 'Yazı əlavə edərkən xəta')
    else:
        form = AddPostForm()
    return render(request, 'univeristy/addpage.html', {'form': form})
    



