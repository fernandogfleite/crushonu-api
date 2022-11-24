from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

from crushonu.apps.authentication.serializers.authentication import JWTSerializer
from crushonu.apps.authentication.views.authentication import UserRegisterViewSet

# JWT Auth
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(serializer_class=JWTSerializer),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('register/',
         UserRegisterViewSet.as_view({'post': 'create'}), name='register_user'),
]
