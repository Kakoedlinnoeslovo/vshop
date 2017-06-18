from django import forms

class EditTextForm(forms.Form):
        text_field = forms.CharField(label='Редактировать текст', max_length=100)
