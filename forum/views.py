
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Branch, Comment, Like
from django.views.decorators.http import require_POST

@login_required
def home_forum(request):
    branches = Branch.objects.all()
    return render(request, 'portal/home_forum.html', {
        'branches': branches
    })

@login_required
def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        media = request.FILES.get('media')
        if content:
            Comment.objects.create(branch=branch, author=request.user, content=content, media=media)
            return redirect('portal:branch_detail', branch_id=branch_id)

    comments = branch.comments.all().order_by('-created_at')
    liked_comment_ids = request.user.liked_comments.values_list('comment_id', flat=True)

    return render(request, 'portal/branch_detail.html', {
        'branch': branch,
        'comments': comments,
        'liked_comment_ids': liked_comment_ids
    })


@login_required
@require_POST
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    like, created = Like.objects.get_or_create(user=request.user, comment=comment)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'likes_count': comment.likes.count()
    })
