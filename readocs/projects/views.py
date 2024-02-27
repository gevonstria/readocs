from django.shortcuts import render, redirect
from django.views.generic import View
from projects.models import Project

class ProjectPageView(View):
    template_name = 'projects.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("/login")

        # get user groups
        user_group = request.user.groups.all()
        projects = Project.objects.filter(allowed_group__in=user_group)
        context = {
            "projects": projects
        }
        return render(request, self.template_name, context=context)

class ProjectApiDocsView(View):
    template_name = 'swagger-ui.html'

    def get(self, request, project_id, project_name):
        if not request.user.is_authenticated:
            return redirect("/login?src=" +request.path)

        project = Project.objects.get(id=project_id)
        context = {
            "project_id": project_id,
            "swagger_file": project.upload.url
        }
        return render(request, self.template_name, context=context)
