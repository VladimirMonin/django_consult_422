from .models import Visit
from django import forms


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["name", "phone", "comment", "master", "services"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Имя"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Телефон"}
            ),
            "comment": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Комментарий"}
            ),
            "master": forms.Select(attrs={"class": "form-control"}),
            "services": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
