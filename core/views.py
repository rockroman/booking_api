from rest_framework.decorators import api_view
from rest_framework.response import Response

# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer


# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer


@api_view()
def root_route(request):
    return Response({"message": "Welcome to Booking API"})
