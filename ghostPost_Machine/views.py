from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostPost_Machine.models import BoastOrRoast
from ghostPost_Machine.forms import AddPost


def index(request):
    feedData = BoastOrRoast.objects.all()
    return render(request, 'index.html', {"feedData": feedData})


def addpost(request):
    html = 'postView.html'
    if request.method == "POST":
        form = AddPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BoastOrRoast.objects.create(
                description=data['description'],
                isBoast=data['isBoast']
            )
            return HttpResponseRedirect('/')
    form = AddPost()
    return render(request, html, {'form': form})


def roastsview(request):
    html = 'roastsView.html'
    roastInfo = BoastOrRoast.objects.filter(isBoast=False)
    return render(request, html, {'roastInfo': roastInfo})


def boastsview(request):
    html = 'boastsView.html'
    boastInfo = BoastOrRoast.objects.filter(isBoast=True)
    return render(request, html, {'boastInfo': boastInfo})


def likesview(request, post_id):
    post = BoastOrRoast.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect('/')


def dislikesview(request, post_id):
    post = BoastOrRoast.objects.get(id=post_id)
    post.likes -= 1
    post.save()
    return HttpResponseRedirect('/')
