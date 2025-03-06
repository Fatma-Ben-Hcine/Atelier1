from django.shortcuts import render, redirect 
from django.forms import ModelForm, Textarea 
from django.contrib import messages 
from django.urls import reverse 
from myform.models import Contact 
 
class ContactForm(ModelForm): 
    def __init__(self, *args, **kwargs): 
        super(ContactForm, self).__init__(*args, **kwargs) 
        self.fields['name'].label = "Nom" 
        self.fields['firstname'].label = "Prénom" 
        self.fields['email'].label = "E-mail" 
 
    class Meta: 
        model = Contact 
        fields = ('name', 'firstname', 'email', 'message') 
        widgets = { 
            'message': Textarea(attrs={'cols': 60, 'rows': 10}), 
        } 
 
def contact(request): 
    form = ContactForm() 
    if request.method == "POST": 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            new_contact = form.save() 
            messages.success( 
                request, f"Nouveau contact : {new_contact.name} {new_contact.email}" 
            ) 
            context = {'pers': new_contact} 
            return render(request,'detail.html', context) 
    # Si méthode GET, on présente le formulaire 
    context = {'form': form} 
 
    return render(request, 'contact.html', context) 
 
def detail(request, cid): 
    contact = Contact.objects.get(pk=cid) 
    context = {'pers': contact} 
    return render(request,'detail.html', context) 
