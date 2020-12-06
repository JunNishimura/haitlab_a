from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer

from user.models import CustomUser
from idea.models import PostIdea, Comment
from event.models import Event
from tag.models import Tag, UserTagMap, IdeaTagMap
from .serializers import UserSerializer, EventSerializer, IdeaSerializer, CommentSerializer, TagSerializer, UserTagMapSerializer, IdeaTagMapSerializer
from .permissions import IsAuthorOrReadOnly

class UserViewset(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.ListModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class EventViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class IdeaViewset(viewsets.ModelViewSet):

    queryset = PostIdea.objects.all()
    serializer_class = IdeaSerializer

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class UserTagMapViewSet(viewsets.ModelViewSet):
    queryset = UserTagMap.objects.all()
    serializer_class = UserTagMapSerializer

class IdeaTagMapViewSet(viewsets.ModelViewSet):
    queryset = IdeaTagMap.objects.all()
    serializer_class = IdeaTagMapSerializer