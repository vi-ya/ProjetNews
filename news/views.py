from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView
from .models import New
from news.forms import NewsForm
# Décorateur login_required
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


# mode class
# class HomePageView(ListView):
#     model = New
#     template_name = "pages/home.html"
#     context_object_name = "home"

# mode fonction
# class NewsPageView(ListView):
#     model = New
#     template_name = "news/news.html"
#     context_object_name = "news_list"

def news_view(request):
    news = New.objects.all()
    return render(request, "news/news.html", {"news_list": news})

# 1. display details of a news article
def news_detail(request, id):  
    # Searches for an object in the database corresponding to the ID supplied.
    news = get_object_or_404(New, id=id)
    # Load the news/new_detail.html page by passing it the article (news) under the name ‘new’. A dictionary containing the data to be sent to the template.
    # {"news": news} {"template name": data}
    return render(request, "news/news_detail.html", {"news": news} )

# Article creation
# Redirects to the login page if the user is not authenticated.
@login_required(login_url=reverse_lazy("login"), redirect_field_name=None)
# It is responsible for displaying a form to create a journal and for processing the submission of the form.
def news_create(request):
    if request.method == 'POST':
        # JournalForm(request.POST): We create a form pre-filled with the data sent by the user (request.POST).
        # JournalForm is a Django form based on the Journal model (defined elsewhere).
        form = NewsForm(request.POST, request.FILES)  # request.FILES it displays the downloaded image 
        # form.is_valid(): checks whether the data entered is correct (e.g. all mandatory fields are filled in). If valid, the form is saved.
        if form.is_valid():
            # form.save() : Creates a new Journal object and automatically saves it in the database. Stores the object in the log so that you can retrieve its id and redirect the user.
            news = form.save()
            # Once the journal has been created, the user is redirected to the page displaying the details of the newly created journal. ‘journal_detail’ is the name of the route defined in urls.py. journal.id is the unique identifier of the newly saved journal.
            return redirect('news_detail', news.id)
    else:
        # If the user simply accesses the creation page, an empty form is displayed.
        form = NewsForm()
        # Displays the HTML page ‘journaux/journal_create.html’. Passes the form to the template so that it is displayed.
    return render(request, 'news/news_create.html', {"form": form})

# update a news article
@login_required(login_url=reverse_lazy("login"), redirect_field_name=None)
def news_update(request, id):
    news = get_object_or_404(New, id=id)  #Finds the New object with the id provided

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news) # Creating a form with the data submitted
        if form. is_valid(): #Checks that the data is correct 
            form.save() #Saves changes in the database.
            
            return redirect('news_detail', news.id) 

    else:
        form = NewsForm(instance=news) #pre-fills the form with the item's current data so that it can be modified.

    return render(request, 'news/news_update.html', {'form':form}) #Affiche le formulaire dans le fichier news_update.html.

@login_required(login_url=reverse_lazy("login"), redirect_field_name=None)
def news_delete(request,id):
    news = get_object_or_404(New, id=id) 
    
    if request.method == 'POST':
        
        news.delete()

        return redirect('news')
    
    return render(request, "news/news_delete.html", {"news":news})