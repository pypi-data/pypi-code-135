from django import forms
from onepage.utils import bootstrap_visible_fields


class ModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ModelForm, self).__init__(*args, **kwargs)
        bootstrap_visible_fields(self.visible_fields)


class Form(forms.Form):
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        bootstrap_visible_fields(self.visible_fields)
