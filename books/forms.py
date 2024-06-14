from django import forms
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.books
        fields = "__all__"
