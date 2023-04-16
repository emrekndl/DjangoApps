from django.urls import include, path
from profiles.api.views import ProfileViewSet, ProfileStateViewSet, ProfileImageUpdateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'user-profiles', ProfileViewSet, basename='profile')
router.register(r'profile-state', ProfileStateViewSet, basename='profile-state')

urlpatterns = [
    path('', include(router.urls)),
    path('profile-image/', ProfileImageUpdateView.as_view(), name='profile-image'),
]


# profile_list = ProfileViewSet.as_view({'get': 'list'})
# profile_detail = ProfileViewSet.as_view({'get': 'retrieve'})

# urlpatterns = [
#     # path("user-profiles/", ProfileList.as_view(), name="profile-list"),
#     path("user-profiles/", profile_list, name="profile-list"),
#     path("user-profiles/<int:pk>", profile_detail, name="profile-detail"),
# ]
