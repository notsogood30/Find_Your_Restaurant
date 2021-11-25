from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def post(request):
    return render(request,'posts/post.html')
# Create your views here.
