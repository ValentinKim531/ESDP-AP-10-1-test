from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from accounts.cookie_auth import CookieJWTAuthentication


class CombinedMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path != reverse('login'):
            raw_refresh_token = request.COOKIES.get('refresh_jwt')

            if raw_refresh_token is not None:
                try:
                    refresh = RefreshToken(raw_refresh_token)
                    new_tokens = refresh.access_token

                    request.COOKIES['jwt'] = str(new_tokens)
                    request.COOKIES['refresh_jwt'] = str(refresh)
                except TokenError as e:
                    if isinstance(e, InvalidToken):
                        return redirect('login')
                    else:
                        print(f"Error while refreshing tokens: {str(e)}")

            auth = CookieJWTAuthentication()
            try:
                auth_result = auth.authenticate(request)
            except InvalidToken:
                return redirect('login')

            if auth_result is not None:
                auth_user, _ = auth_result
                if auth_user is not None:
                    request.user = auth_user
