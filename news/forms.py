from django import forms
from .models import New

# forms.ModelForm is used to create a form that corresponds to a Django model.
class NewsForm(forms.ModelForm):
    # Meta is a subclass used to configure the form.
    # fields = ‘all’ → Indicates that all fields in the New model will be included in the form.
    class Meta:
        model = New
        fields = '__all__'