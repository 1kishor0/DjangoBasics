from django import forms
from django.core import validators
from first_app.models import Album,Musician
# class new_form(forms.Form):
#     username = forms.CharField(required=False, max_length=100)
#     email=forms.EmailField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Please enter your email','style':'width:300px'}))
#     password = forms.CharField(initial=1234,max_length=15,min_length=5)
#     user_dob=forms.DateField(label='Birthdate', required=False,widget=forms.TextInput(attrs={'type':'date'}))
   
#    #widget=forms.RadioSelect
#     choiceField=forms.MultipleChoiceField(choices=((1, 'first'), (2, 'second'), (3, 'third'), (4, 'fourth'), (5, 'fifth'),),widget=forms.CheckboxSelectMultiple)
#     boolean_field = forms.BooleanField(required=False)
# #for validators in validators
# def evenOrOdd(value):
#     if value % 2 == 1:
#         raise forms.ValidationError("Please insert an even number")
# class secondForm(forms.Form):
#     nnumber_field=forms.IntegerField(validators=[evenOrOdd])
#     user_email=forms.EmailField()
#     user_vmail=forms.EmailField()

#     def cleans(self):
#      all_cleaned_data = super().clean()
#      user_email=all_cleaned_data['user_email']
#      user_vmail=all_cleaned_data['user_vmail']

#      if user_email!=user_vmail:
#          raise forms.ValidationError("Please enter the same email")

# //musician format

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"