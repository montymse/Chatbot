from django import forms

from .models import Room


class RoomForm(forms.ModelForm):
    navn = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Indtast navn for at forsætte"})
    )

    class Meta:
        model = Room
        fields = [
            'navn',
        ]
