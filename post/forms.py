from django import forms
from .models import Comment


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-4'}),
            'email': forms.TextInput(attrs={'class': 'form-control col-4'}),
            'body': forms.TextInput(attrs={'class': 'form-control col-4'})
        }


class EmailForm(forms.Form):

    to_id = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    to_name = forms.CharField(widget=forms.TimeInput(attrs={'class': 'form-control'}))