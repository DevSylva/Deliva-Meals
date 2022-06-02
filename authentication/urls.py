from django.urls import path
from authentication.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from authentication.views import MyObtainTokenPairView, RegisterView, LogoutView


app_name = "authentication"

urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', LogoutView.as_view(), name="logout"),
]