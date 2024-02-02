from django.shortcuts import render, redirect
from django.views.generic import View

class ProjectPageView(View):
    template_name = 'projects.html'

    def get(self, request):
        return render(request, self.template_name, context={})
