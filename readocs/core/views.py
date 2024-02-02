from django.shortcuts import render, redirect
from django.views.generic import View
from projects.views import ProjectPageView

class LoginPageView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name, context={})

    def post(self, request):
        print(request.POST.get("username"))
        return redirect("/projects")
