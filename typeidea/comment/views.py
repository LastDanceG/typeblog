# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect

# Create your views here.
from django.views.generic import TemplateView

from comment.forms import CommentForm
from comment.models import Comment


class CommentShowMixin(object):
    def get_comment(self):
        target = self.request.path
        comments = Comment.objects.filter(target=target)
        return comments

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(),
            'comment_list': self.get_comment()
        })
        return super(CommentShowMixin, self).get_context_data(**kwargs)


class CommentView(TemplateView):
    http_method_names = ['POST']
    template_name = 'comment/result.html'

    def get(self, request, *args, **kwargs):
        return super(CommentView, self).get(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')
        context = {}
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False
        context.update({
            'succeed': succeed,
            'form': comment_form,
            'target': target
        })
        return self.render_to_response(context)