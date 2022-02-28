from django import forms
 
class uploadImage(forms.Form):
    upload_image = forms.ImageField()

    