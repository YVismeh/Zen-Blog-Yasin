from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Blog, Agent
from .forms import ContactUsForm
from django.contrib import messages

# Create your views here.

class HomeView(TemplateView):
    template_name = "root/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog"] = Blog.objects.all()[:4]
        return context
    

def contact_us(request):
    if request.method == "POST" :
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "successfully created contact")
            return render(request, 'root/contact.html')
        else:
            messages.add_message(request, messages.ERROR, "data invalid")
            return render(request, 'root/contact.html')
    else:
        return render(request, "root/contact.html")
    

class AboutView(TemplateView):
    template_name = "root/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["agents"] = Agent.objects.all(status=True)[:4]
        return context