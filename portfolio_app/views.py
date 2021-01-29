from django.shortcuts import render

# Create your views here.
from .forms import CommentForm

def post_detailview(request, id):
  if request.method == 'POST':
    cf = CommentForm(request.POST or None)
    if cf.is_valid():
      content = request.POST.get('content')
      comment = Comment.objects.create(post = post, user = request.user, content = content)
      comment.save()
      return redirect(post.get_absolute_url())
    else:
      cf = CommentForm()

    context ={
      'comment_form':cf,
      }
    return render(request, 'socio / post_detail.html', context)
