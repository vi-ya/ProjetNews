# from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from news.models import New

# # class HomePageView(TemplateView):  
# #   template_name = "pages/home.html"

# # class HomePageView(ListView): 
# #   model = New 
# #   template_name = "pages/home.html"
# #   context_object_name = "home"

# def home_view(request):
#   news = New.objects.all()
#   return render(request, "pages/home.html", {"home_list": news})

# # def section_list(request):
# #   section_list = New.objects.filter(section="INFORMATIONS")[:3]
# #   return render(request, "pages/home.html", {"section_list": section_list})

# def list_view(request):
#   list_view = New.objects.filter(section="INFORMATIONS")[:4]  # Filtre et limite à 4
#   return render(request, "pages/home.html", {"list_list": list_view})


def home_view(request):
    news = New.objects.all()  #  Get all news
    section_view_informations = New.objects.filter(section="Informations")[:4]  #  Filter for 4 items "INFORMATION
    section_view_ressources = New.objects.filter(section="Ressources")[:4]  
    section_view_evenements = New.objects.filter(section="Événements")[:4]  
    section_view_opportunites = New.objects.filter(section="Opportunités")[:4]  
    section_view_profiles = New.objects.filter(section="Profils")[:4]  
    
    return render(request, "pages/home.html", {
        "home_list": news,
        "section_view_informations": section_view_informations,  
        "section_view_ressources": section_view_ressources, 
        "section_view_evenements": section_view_evenements,  
        "section_view_opportunites": section_view_opportunites,  
        "section_view_profiles": section_view_profiles, 
    })

class AboutPageView(TemplateView):  
    template_name = "pages/about.html"

class Error404View(TemplateView):
    template_name = "pages/404.html"

   
