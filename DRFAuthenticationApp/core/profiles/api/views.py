from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile, ProfileState
from profiles.api.serializers import ProfileSerializer, ProfileStateSerializer, ProfileImageSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, generics
from rest_framework.filters import SearchFilter
from profiles.api.permissions import IsOwnerOrReadOnly, IsOwnerStateOrReadOnly


# class ProfileList(generics.ListAPIView):
# class ProfileViewSet(ReadOnlyModelViewSet):
class ProfileViewSet(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    """ List all profiles. """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('city',)


class ProfileStateViewSet(ModelViewSet):
    """ List profile states. """

    # queryset = ProfileState.objects.all()
    serializer_class = ProfileStateSerializer
    permission_classes = (IsAuthenticated, IsOwnerStateOrReadOnly,)

    def get_queryset(self):
        queryset = ProfileState.objects.all()
        if user_name := self.request.query_params.get('username', None):
            queryset = queryset.filter(user_profile__user__username=user_name)

        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)

        return super().perform_create(serializer)


class ProfileImageUpdateView(generics.UpdateAPIView):
    """ Update profile image. """

    serializer_class = ProfileImageSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile
