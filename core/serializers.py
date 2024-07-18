# from rest_framework_simplejwt.serializers import TokenRefreshSerializer
# from rest_framework_simplejwt.serializers import TokenRefreshSerializer


# class CustomTokenRefreshSerializer(TokenRefreshSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         data["refresh"] = attrs["refresh"]  # Include the refresh token in the response
#         return data
