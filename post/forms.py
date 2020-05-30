from django import forms
from .models import Comment


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


class EmailForm(forms.Form):

    to_id = forms.EmailField(widget=forms.EmailInput())
    to_name = forms.CharField(widget=forms.TimeInput())

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control col-4',
            })
