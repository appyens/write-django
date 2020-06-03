from django import forms
from .models import Comment
from django.core.exceptions import ValidationError
import string


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control col-4',
            })

    def save(self, commit=True):
        pass


class EmailForm(forms.Form):

    to_id = forms.EmailField(widget=forms.EmailInput())
    to_name = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control col-10',
            })

    def clean_to_name(self):
        name = self.cleaned_data.get('to_name')
        if any(ch in name for ch in string.punctuation):
            raise ValidationError("Please enter valid name")
        return name
