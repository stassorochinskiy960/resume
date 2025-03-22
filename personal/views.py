from django.shortcuts import render
from .models import Image, Experience, Education, Project, PositionPerson

#file work
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404

# Create your views here.
def personal(request):

    image = Image.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    project = Project.objects.all()
    positionPerson = PositionPerson.objects.all()
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