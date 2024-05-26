from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import requests
from django.conf import settings



class SSOAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION')
        if(auth is None):
            return None

        response = requests.get(f"{settings.SSO_BACKEND_URL}/api/get-user-info/", {}, headers={'Authorization': auth})

        if response.status_code == 200:
            user_info = response.json() #{'username':'nhrnhr0''organization':'org12''type':'editor'}
            # make sure that user_info.domain is the same as our domain
            # user_domain =user_info.get('domain', 'http://no-domain').split('//')[1]
            backend_domain = user_info.get('backend_domain', 'http://no-domain').split('//')[1]
            frontend_domain = user_info.get('frontend_doamin', 'http://no-domain').split('//')[1]
            if not (backend_domain == request.META.get('HTTP_HOST') or frontend_domain == request.META.get('HTTP_HOST')):
                raise AuthenticationFailed('user organization does not match the request domain: %s / %s != %s' % (backend_domain,frontend_domain, request.META.get('HTTP_HOST')))
            try:
                user = User.objects.get(username=user_info['username'])
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=user_info['username'],
                    first_name=user_info.get('first_name', ''),
                    last_name=user_info.get('last_name', ''),
                    email=user_info.get('email', '')
                )
            user.user_type = user_info['type']
            return user, None
        raise AuthenticationFailed('Invalid token')
