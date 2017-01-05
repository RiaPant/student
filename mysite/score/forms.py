from django import forms
from .models import Person


class Personform(forms.ModelForm):
    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'marks',
            'enroll_no',
        )

        # first_name = forms.CharField(max_length=30)
        # last_name = forms.CharField(max_length=30)
        # marks = forms.IntegerField()
        # enroll_no = forms.CharField(max_length=9)
