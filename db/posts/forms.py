from django import forms


class NameForm(forms.Form):
    your_task = forms.CharField(label='', max_length=35)