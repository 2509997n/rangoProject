from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForms):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(wideget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(wideget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(wideget=forms.HiddenInput(), required=False)

    #an inline class to provide additional information in the form
    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(wideget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)