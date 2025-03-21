from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from oauth2_provider.decorators import protected_resource

def hello_world(request):
    return HttpResponse("Hello, World!")

@protected_resource()
def protected_view(request):
    return HttpResponse("Cette page est protégée via Keycloak. Vous devez être authentifié pour y accéder.")

