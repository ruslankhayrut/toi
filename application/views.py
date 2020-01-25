from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
def index(request):
    return render(request, 'application/index.html')

def registration(request):
    return render(request, 'application/registration.html')




def act(request):
    if '_login' in request.POST:
        return HttpResponseRedirect(reverse('login'))
    elif '_register' in request.POST:
        return HttpResponseRedirect(reverse('application:registration'))
