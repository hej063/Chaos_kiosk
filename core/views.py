from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import PostForm, CardForm
from .models import Post, Card

def default(request):
    return render(request, 'core/default.html')

def menu(request):
    posts = Post.objects.order_by('title')
    if request.method == "POST":
        for i, post in enumerate(posts):
            if i == 0 :
                form1 = PostForm(request.POST, request.FILES, instance=post)
                if form1.is_valid():
                    post = form1.save()
            elif i == 1 :
                form2 = PostForm(request.POST, request.FILES, instance=post)
                if form2.is_valid():
                    post = form2.save()
            elif i == 2 :
                form3 = PostForm(request.POST, request.FILES, instance=post)
                if form3.is_valid():
                    post = form3.save()
        return redirect('menu')

    else: #request.GET()
        for i, post in enumerate(posts):
            if i == 0:
                form1 = PostForm(instance=post)
            elif i == 1:
                form2 = PostForm(instance=post)
            elif i == 2:
                form3 = PostForm(instance=post)
        forms =[form1, form2, form3]
        ctx = {'posts':posts, 'forms':forms}
        return render(request, 'core/menu.html', ctx)

def payment(request):
    if request.method == "POST":
        form = CardForm(request.POST, request.FILES)
        if "카드" in str(request.FILES['photo']):
            return redirect('complete')
        
        else:
            return redirect('payment')

        # print(request.FILES['photo'])
        # if form.is_valid():
        #     card = form.save()
        #     return redirect('payment')
    else:
        form = CardForm()
        card = Card.objects.get(pk=26)
    return render(request, 'core/payment.html', {'card':card, 'form': form})

def complete(request):
    posts = Post.objects.order_by('title')
    for post in posts:
        post.count = 0
        post.save()
    return render(request, 'core/complete.html')