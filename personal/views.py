from django.shortcuts import render
from .models import Ip, Image, Experience, Education, Project, PositionPerson

#file work
from django.http import FileResponse, Http404,HttpRequest
from django.shortcuts import get_object_or_404

def get_client_ip(request: HttpRequest):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip

# Create your views here.
def personal(request):

    image = Image.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    project = Project.objects.all()
    positionPerson = PositionPerson.objects.all()

    # views request
    ip = get_client_ip(request)
    Ip.objects.create(ip_address=ip)

    return render(request, 'personal/personal.html', {'image': image,
                                                      'experience': experience, 'education': education,
                                                      'project': project, 'positionPerson': positionPerson})

def download_file(request, file_id):
    # dock req
    document = get_object_or_404(Image, id=file_id)
    try:
        return FileResponse(document.file.open('rb'), as_attachment=True, filename=document.file.name)
    except FileNotFoundError:
        raise Http404("File not found")