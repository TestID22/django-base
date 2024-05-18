from django import forms


class NameForm(forms.Form):
    your_task = forms.CharField(label='', max_length=35)


class EmailMessageForm(forms.Form):
    name = forms.CharField(label="Name*", max_length=10)
    email_adress = forms.EmailField(label='Email*', max_length=20)
    message = forms.CharField(label="Text", max_length=100)