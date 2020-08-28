from django import forms


class ContactFrom(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your notes or questions here...'}))
