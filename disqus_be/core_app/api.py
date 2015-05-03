"""This module contains API resource classes"""
from tastypie.resources import ModelResource
from core_app.models import *
from tastypie.authorization import Authorization
from tastypie import fields


class SiteResource(ModelResource):
    url = fields.CharField(attribute="url", use_in="list")
    comment = fields.ToManyField(
        'disqus_be.core_app.api.CommentsResource',
        'comment_set', null=True, use_in="detail", full=True)

    class Meta:
        queryset = Site.objects.all()
        resource_name = 'site'
        authorization = Authorization()
        always_return_data = True


class CommentsResource(ModelResource):
    login = fields.CharField(attribute="login", use_in="list")
    email = fields.CharField(attribute="email", use_in="list")
    pub_date = fields.CharField(attribute="pub_date", use_in="list")
    message = fields.CharField(attribute="message", use_in="list")
    site = fields.ToOneField('disqus_be.core_app.api.SiteResource', 'site')

    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        always_return_data = True
