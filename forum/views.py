
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Branch, Comment, Like
from django.views.decorators.http import require_POST
from django.db.models import Count
from config.utils import extract_youtube_video_id

@login_required
def home_forum(request):
    branches = Branch.objects.all()
    return render(request, 'forum/home_forum.html', {
        'branches': branches
    })

@login_required
def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        media = request.FILES.get('media')
        parent_id = request.POST.get('parent_id')
        parent_comment = Comment.objects.filter(id=parent_id).first() if parent_id else None

        if content:
            youtube_video_id = extract_youtube_video_id(content)
            Comment.objects.create(
                branch=branch,
                author=request.user,
                content=content,
                media=media,
                parent=parent_comment,
                youtube_video_id=youtube_video_id
            )
            return redirect('forum:branch_detail', branch_id=branch_id)

    comments = branch.comments.filter(parent__isnull=True).order_by('-created_at')
    liked_comment_ids = request.user.liked_comments.values_list('comment_id', flat=True)

    return render(request, 'forum/branch_detail.html', {
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

@login_required
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    branch_id = comment.branch.id
    comment.delete()
    return redirect('forum:branch_detail', branch_id=branch_id)