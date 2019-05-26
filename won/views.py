from django.shortcuts import render

# Create your views here.
def index(request):
    current_user = request.user
    projects = Project.get_all()
    return render(request,'index.html',{'projects':projects})

def project(request,project_id):
    project = Project.objects.get(id = project_id)
    rating = round(((project.design + project.usability + project.content)/3),2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            if project.design == 1:
                project.design = int(request.POST['design'])
            else:
                project.design = (project.design + int(request.POST['design']))/2
            if project.usability == 1:
                project.usability = int(request.POST['usability'])
            else:
                project.usability = (project.design + int(request.POST['usability']))/2
            if project.content == 1:
                project.content = int(request.POST['content'])
            else:
                project.content = (project.design + int(request.POST['content']))/2
            project.save()
    else:
        form = VoteForm()
    return render(request,'project.html',{'form':form,'project':project,'rating':rating})