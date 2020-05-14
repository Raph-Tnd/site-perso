from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, 'html/home.html')

def contact(request):
    return render(request, 'html/contact.html')
    
def features(request):
    return render(request, 'html/features.html')

def CV(request):
    return render(request, 'html/CV.html')

def DL(request):
    content = open(os.path.join("/appCV/static/files/CV.pdf")).read()
    response = HttpResponse(content, content_type='application/pdf')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachement; filename=%s' % 'CV.pdf'
    return response

def redirect_view(request):
    response = redirect('/info/')
    return response
