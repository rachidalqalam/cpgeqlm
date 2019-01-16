from django import forms
from django.contrib.auth.models import User

from .models import Module, Eleve


class ItemForm(forms.ModelForm):
    module = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Module.objects.all())
    class Meta:
        model = Module
        fields = '__all__'