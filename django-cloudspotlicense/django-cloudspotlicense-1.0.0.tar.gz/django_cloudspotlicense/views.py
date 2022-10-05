import json
from http import HTTPStatus

from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.contrib.auth import login, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from cloudspotlicense.api import CloudspotLicense_API
from cloudspotlicense.constants.errors import BadCredentials
from cloudspotlicense.constants.responses import ResponseStatus

from .models import GlobalPermission, CloudspotCompany
from .helpers import revoke_permissions, grant_permissions

class LoginView(View):
    """ Authenticates the user against the Cloudspot License Server """
    
    template_name = 'auth/login.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        redirect_url = settings.LOGIN_REDIRECT_URL if hasattr(settings, 'LOGIN_REDIRECT_URL') else '/'
        login_url = settings.LOGIN_URL if hasattr(settings, 'LOGIN_URL') else '/'
        
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        # We authenticate using the License Server
        api = CloudspotLicense_API(settings.CLOUDSPOT_LICENSE_APP)
        try:
            api.authenticate(username, password)
        except BadCredentials:
            messages.error(request, _('Email or password incorrect'))
            return redirect(login_url)
        
        # Gather the additional user info from the API
        api.get_user()
        
        # First check if we know the company, if not, we create it if it is present in the response
        company = None
        if api.user.company_id:
            company = CloudspotCompany.objects.filter(id=api.user.company_id).first()
            if not company: company = CloudspotCompany.objects.create(id=api.user.company_id, name=api.user.company_name)
            elif company.name != api.user.company_name:
                company.name = api.user.company_name
                company.save()
            
        # Then we check if we know the user in our system
        UserModel = get_user_model()
        try:
            # Update the user with the new information
            user = UserModel.objects.get(username=username)
            user.first_name = api.user.first_name
            user.last_name = api.user.last_name
            user.license_token = api.token
            user.is_active = True
            user.company = company
            user.save()
        except ObjectDoesNotExist:
            
            # We don't know the user, so we create them
            # Push it to the database
            user = UserModel.objects.create_user(username=username, email=username, password=password, **{
                'first_name' : api.user.first_name,
                'last_name' : api.user.last_name,
                'license_token' : api.token,
                'company' : company
            })
            
            user.save()
        
        # Remove all existing permissions
        revoke_permissions(user)
        
        # Assign all the returned permissions
        permissions = []
        for perm in api.permissions.items(): permissions.append(perm.permission)
        grant_permissions(user, permissions)
        
        # Finally, we log them in and redirect them
        login(request, user)
        
        return redirect(redirect_url)
    
@method_decorator(csrf_exempt, name='dispatch')
class WebhookView(View):
    """ Handles all the webhook events that the Cloudspot License Server server sends """
    
    def post(self, request, *args, **kwargs):
        
        req = json.loads(request.body)
        event = req['event']
        data = req['data']
        UserModel = get_user_model()
        
        if event == 'permissions.updated':
            token = data['token']
            user = UserModel.objects.filter(license_token=token).first()
            if not user: return JsonResponse({ 'status' : ResponseStatus.NOT_FOUND, 'error' : { 'message' : 'No user matched the token.' }}, status=HTTPStatus.NOT_FOUND)
            
            permissions = data['permissions']
            revoke_permissions(user)
            
            if 'use_app' not in permissions:
                user.is_active = False
                user.save()
            else:
                grant_permissions(user, permissions)

            return JsonResponse({ 'status' : ResponseStatus.OBJECT_UPDATED })