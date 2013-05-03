from tastypie.authorization import ReadOnlyAuthorization
from tastypie.resources import ModelResource
from xiaonuogantan.models import Comment, Post

class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization = ReadOnlyAuthorization()
