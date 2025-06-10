from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nom",
        max_length=30,
        required=True,
        error_messages={'required': 'Veuillez entrer votre nom.'},
        widget=forms.TextInput(attrs={
            'placeholder': 'DUBOIS',
            'class': 'first_name'})
    )

    last_name = forms.CharField(
        label="Prénom",
        max_length=30,
        required=True,
        error_messages={'required': 'Veuillez entrer votre prénom.'},
        widget=forms.TextInput(attrs={
            'placeholder': 'Paul',
            'class': 'last_name'})
    )

    email = forms.EmailField(
        label="Email",
        max_length=254,
        required=True,
        error_messages={'required': 'Veuillez entrer une adresse e-mail valide.'},
        widget=forms.EmailInput(attrs={
            'placeholder': 'toto@hotmail.com',
            'class': 'email_name'})
    )

    username = forms.CharField(
        label="Nom d'utilisateur",
        max_length=25,
        required=True,
        error_messages={
            'required': 'Veuillez entrer un nom d\'utilisateur.',
            'invalid': "Ce nom d'utilisateur est invalide."
        },
        widget=forms.TextInput(attrs={
            'style': 'border-color: blue;',
            'placeholder': 'Toto',
            'class': 'username'})
    )

    password1 = forms.CharField(
        label="Mot de passe",
        max_length=50,
        required=True,
        min_length=8,
        error_messages={
            'required': 'Veuillez entrer un mot de passe.',
            'min_length': "Votre mot de passe doit contenir au moins 8 caractères."
        },
        widget=forms.PasswordInput(attrs={
            'placeholder': 'aA@8#z9&',
            'class': 'password1'})
    )

    password2 = forms.CharField(
        label="Confirmez le mot de passe",
        max_length=50,
        required=True,
        error_messages={'required': 'Veuillez confirmer votre mot de passe.'},
        widget=forms.PasswordInput(attrs={
            'placeholder': 'aA@8#z9&',
            'class': 'password2'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        print("Validation du nom d'utilisateur:", username)  #  debug console
        forbidden_usernames = ["admin", "root", "superuser"]
        if username in forbidden_usernames:
            raise forms.ValidationError("Ce nom d'utilisateur est interdit.")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ce nom d'utilisateur est déjà utilisé.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet e-mail est déjà utilisé.")
        return email
    
      # 
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")

        return password2

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if username and email and username.lower() == email.split('@')[0].lower():
            self.add_error('username', "Le nom d'utilisateur ne peut pas être identique à l'email.")

        return cleaned_data



        
