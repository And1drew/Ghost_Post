from django import forms


class AddPost(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    isBoast = forms.BooleanField(required=False)
