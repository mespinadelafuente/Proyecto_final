from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import request
from Pages.models import Comment
from Pages.models import Post
from Pages.forms2 import CommentForm , PostForm
 
 
class PostListView (ListView):
    model = Post
    paginate_by = 3

 
 
class PostDetailView(DetailView):
    model = Post
    template_name = "pages/post_detail.html"
    fields = ["name", "code", "description"]
 
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=post).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)
 
 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("pages:post-list")
 
    form_class = PostForm
    # fields = ["name", "code", "description", "image"]
 
    def form_valid(self, form):
        """Filter to avoid duplicate posts"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Post.objects.filter(
            name=data["name"], code=data["code"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El post {data['name']} - {data['code']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Post {data['name']} - {data['code']} creado exitosamente!",
            )
            return super().form_valid(form)
 
 
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["name", "code", "description", "image"]
 
    def get_success_url(self):
        post_id = self.kwargs["pk"]
        return reverse_lazy("pages:post-detail", kwargs={"pk": post_id})
 
 
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("pages:post-list")
 
 
class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, post=post
        )
        comment.save()
        return redirect(reverse("pages:post-detail", kwargs={"pk": pk}))
 
 
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
 
    def get_success_url(self):
        post = self.object.post
        return reverse("pages:post-detail", kwargs={"pk": post.id})


# Create your views here.
