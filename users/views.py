from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm (change to add more items)
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import SignUpForm
 # Formulaire personnalisé


# Create a user
def register_view(request):

    if request.method == "POST": 

        # form = UserCreationForm(request.POST) #A form bound to the POST data  
        # form = (request.POST) #A form bound to the POST data

        if form. is_valid(): # All validation rules pass
            # form.save()  
            
            login(request, form.save())   #Connects users automatically / User registration
            # return redirect("news_list: news ") # Redirect after POST  
            messages.success(request, "Inscription réussie ! Bienvenue 👋")
            return redirect("home") # Redirects to the home page
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else: 
        # form = UserCreationForm()  # An unbound form  
        form = SignUpForm()  # An unbound form

    return render(request, "users/register.html", {"form": form})


def login_view(request): 
    if request.method == "POST": 
           
        # form = UserCreationForm() 
        form = AuthenticationForm(data=request.POST) # Django checks that the identifiers are correct.
        
        if form.is_valid(): #It performs automatic validation. / Checks that the information is correct (valid user name and password).
            user = form.get_user()
            login(request, user)
           
            # next : Redirect to the page initially requested by the user.
            next_url = request.GET.get('next', 'home')
            messages.success(request, f"Bienvenue, {user.username} !")
            return redirect(next_url)
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        
    else:
     
        form = AuthenticationForm() #Creates an empty form for the user to enter their login details
   
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Vous avez été déconnecté avec succès.")
        return redirect("home")
  

