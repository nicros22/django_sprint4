from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from .models import Post, Comment

User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'created_at',)
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

        def clean(self):
            super().clean()
            send_mail(
                subject="Новый пост",
                message=f"Новый пост: \"{self.cleaned_data.get('title')}\"."
                f"Название: {self.cleaned_data.get['title']}.",
                from_email="blogicum_project@blogicum.org",
                recipient_list=["admin@blogicum.org"],
                fail_silently=True,
            )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
