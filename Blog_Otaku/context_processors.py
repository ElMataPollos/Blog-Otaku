from multiprocessing import context
from django.contrib.auth.models import User

#Definición de contextos de los datos
def project_context(request):

    context = {
        'me': User.objects.first(),
    }

    return context #String