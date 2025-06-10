from django.shortcuts import render, redirect
# from contacts.forms import ContactUsForm
from django.core.mail import EmailMessage
from django.contrib import messages 

# version send_mail
# def contact(request):

#     # Methode http
#     if request.method == "POST":
#         form = ContactUsForm(request.POST)

#         # Valider les données
#         if form.is_valid():
#             send_mail(
#                 subject=f'Message from {form.cleaned_data['name'] or "anonyme"}',
#                 message=form.cleaned_data['message'],
#                 from_email=form.cleaned_data['email'],
#                 recipient_list=['admin@toto.com']
#             )

#             return redirect('email_sent')
#     else:
#         form = ContactUsForm() # Afficher formulaire vide
        

#     return render(request, 'contacts/contact.html', {'form': form})

# #  Vue pour la page de confirmation d'envoie 
# def email_sent(request):
#     return render(request, "contacts/email_sent.html")

# version EmailMessage
def contact(request):
    # Deletes all existing messages before processing the request
    # storage = messages.get_messages(request)
    # storage.used = True

   # Checks whether the request is POST
    if request.method == "POST":
        try:
            #  Retrieve form data with default values to avoid KeyError
            # .get() added to avoid KeyError.
            # .strip() to avoid unnecessary spaces.
            name = str(request.POST.get("name", "").strip())
            first_name = str(request.POST.get("first_name", "").strip())
            email_address = request.POST.get("email_address", "").strip() 
            message = request.POST.get("message", "").strip()

            # Checks if email and message are provided
            if not email_address or not message:
                messages.error(request, "L'email et le message sont obligatoires.")
                return redirect("contact")  # Redirects to contact page in case of error          

            # E-mail creation
            email = EmailMessage(
                # subject="J'ai une question.", 
                subject=f"Message de l'utilisateur\b{name}", 
                body=f"{name}\b{first_name}\n{email_address}\n\n{message}",
                from_email=email_address,
                to=['ya.vi.dev.pro@gmail.com'],
                reply_to=[email_address],
                headers={'Message-ID': 'foo'},
                
            )
            # Sending email
            email.send(fail_silently=False)

            # messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('email_sent')
        
        # except Exception as e:
            # messages.error(request, f"Une erreur est survenue : {str(e)}")
        except Exception :
            messages.error(request, f"Une erreur est survenue ")

            return redirect("contact")  # Redirect on failure        
    return render(request, 'contacts/contact.html')

#  View for send confirmation page
def email_sent(request):
    return render(request, "contacts/email_sent.html")
