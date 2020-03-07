# -*- coding: utf-8 -*-
from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):

    email = forms.CharField(
        max_length=50,
        label="邮箱",
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width: 60%'}
        ),
    )
    nickname = forms.CharField(
        max_length=30,
        label="昵称",
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width: 60%'}
        ),
    )
    website = forms.CharField(
        max_length=100,
        label="网站",
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width: 60%'}
        ),
    )
    content = forms.CharField(
        label="内容",
        max_length=500,
        widget=forms.widgets.Textarea(
            attrs={'rows': 5, 'cols': 90, 'class': 'form-control'}
        ),
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('评论字数太少啦，多写点！')
        return content

    class Meta:
        model = Comment
        fields = [
            'nickname', 'email', 'website', 'content'
        ]
