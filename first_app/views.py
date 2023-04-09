from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app import forms
# Create your views here.

def index(request):
        #query
        musician_list=Musician.objects.order_by('firstName')
    # return HttpResponse("<h1> I am from first app.</h1> <a href='/contact/'>Contact</a> <a href='/about/'>About</a>")
        diction={'text1': 'This is a list of Musicians','musician':musician_list}
        return render(request,'first_app/index.html',context=diction)

def contact(request):
    return HttpResponse("<h1> This is contact page.</h1><a href='/index/'>Home</a> <a href='/about/'>About</a>")

def about(request):
    return HttpResponse("<h1> This is about page.</h1> <a href='/contact/'>Contact</a> <a href='/index/'>Home</a>") 


# def form1(request):
    
#      new_form=forms.new_form()
#      diction = {'test_form': new_form,'heading': "This form created by django"}

#      if request.method == 'POST':
#           new_form = forms.new_form(request.POST)
#           if new_form.is_valid():
#                username=new_form.cleaned_data['username']
#                password=new_form.cleaned_data['password']
#                email=new_form.cleaned_data['email']
#                user_dob=new_form.cleaned_data['user_dob']
#                choiceField=new_form.cleaned_data['choiceField']
#                bool_field=new_form.cleaned_data['boolean_field']
               
#                diction.update({'username': username, 'password': password, 'email': email, 'user_dob': user_dob,'form_submitted': "Yes",'bool_field':bool_field,'choiceField':choiceField})
#      return render(request,'first_app/form.html',context=diction)
# def form(request):   
#     second_form=forms.secondForm()
#     diction2 = {'test_form2': second_form,'heading2': "This second form created by django"}           
#     if request.method == 'POST':
          
#           second_form=forms.secondForm(request.POST)  
#           diction2.update({'test_form2': second_form})
#           if second_form.is_valid():
#                numberFiled=second_form.cleaned_data['nnumber_field']
#                diction2.update({'user_email':"Fields Match"})
#                diction2.update({'nnumber_field':numberFiled,'form_submitted2':"Yes"})
#     return render(request,'first_app/form.html',context=diction2)

# //For musician form              
    
def form(request):
     new_form=forms.MusicianForm()
     
     if request.method == 'POST':
          new_form = forms.MusicianForm(request.POST)

          if new_form.is_valid():
               new_form.save(commit=True)
               return index(request)
     diction={'test_form': new_form,'heading1':'Add New Musician'}
