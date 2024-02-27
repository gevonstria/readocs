from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from projects.views import ProjectPageView

class LoginPageView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name, context={})

    def post(self, request):
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            if "src" in request.GET:
                return redirect(request.GET["src"])
            else:
                return redirect("/")
        else:
            context = {
                "message": "Invalid Credentials"
            }
            return render(request, self.template_name, context=context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login")
