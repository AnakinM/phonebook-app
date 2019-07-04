from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Person, Phone, Email
from .forms import PersonModelForm, PhoneModelForm, EmailModelForm

# Show all contacts
def contact_list_view(request):
    # Changing None to empty string is just for estetic view while viewing contacts.

    contacts = Person.objects.all() 
    for contact in contacts:
        try:
            contact.phone = contact.phone_set.get(person=contact).phone
            if contact.phone == None: contact.phone = ""
            contact.email = contact.email_set.get(person=contact).email
            if contact.email == None: contact.email = ""
        except Phone.DoesNotExist:
            print("phone does not exist")
        except Email.DoesNotExist:
            print("email does not exist")

    context = {"contacts": contacts}
    return render(request, "contacts/list.html", context)


# Show specific contact
def contact_detail_view(request, id):
    contact = Person.objects.get(pk=id)
    try:
        contact.phone = contact.phone_set.get(person=contact).phone
        if contact.phone == None: contact.phone = ""
        contact.email = contact.email_set.get(person=contact).email
        if contact.email == None: contact.email = ""
    except Phone.DoesNotExist:
        print("phone does not exist")
    except Email.DoesNotExist:
        print("email does not exist")

    context = {"contact": contact}
    return render(request, "contacts/details.html", context)


# Add new contact
def contact_add_view(request):
    if request.method == 'POST':
        person_form = PersonModelForm(request.POST or None)
        phone_form = PhoneModelForm(request.POST or None)
        email_form = EmailModelForm(request.POST or None)

        if person_form.is_valid() and phone_form.is_valid() and email_form.is_valid():
            person = Person.objects.create(**person_form.cleaned_data)
            phone = Phone.objects.create(person=person, phone=phone_form.cleaned_data['phone'])
            email = Email.objects.create(person=person, email=email_form.cleaned_data['email'])
            
            person_form = PersonModelForm()
            phone_form = PhoneModelForm()
            email_form = EmailModelForm()
            return redirect('contact-list')
    else:
        person_form = PersonModelForm()
        phone_form = PhoneModelForm()
        email_form = EmailModelForm()

    context = {'person_form': person_form, 'phone_form': phone_form, 'email_form': email_form}
    return render(request, "contacts/create.html", context)


# Edit contact
def contact_update_view(request, id):
    contact = Person.objects.get(pk=id)
    if Phone.objects.filter(person=contact):
        contact_phone = Phone.objects.get(person=contact)
    else:
        contact_phone = Phone(person = contact, phone=None)
    if Email.objects.filter(person=contact):
        contact_email = Email.objects.get(person=contact)
    else:
        contact_email = Email(person = contact, email=None)

    if request.method == 'POST':
        person_form = PersonModelForm(request.POST or None, instance=contact)
        phone_form = PhoneModelForm(request.POST or None, instance=contact_phone)
        email_form = EmailModelForm(request.POST or None, instance=contact_email)

        if person_form.is_valid() and phone_form.is_valid() and email_form.is_valid():
            person_form.save()
            phone_form.save()
            email_form.save()
        return redirect('contact-list')
    else:
        person_form = PersonModelForm(instance=contact)
        phone_form = PhoneModelForm(instance=contact_phone)
        email_form = EmailModelForm(instance=contact_email)
    context = {'person_form': person_form, 'phone_form': phone_form, 'email_form': email_form, 'id': id}
    return render(request, "contacts/update.html", context)


# Delete contact
def contact_delete_view(request, id):
    contact = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
        if Phone.objects.get(person=contact).phone or Email.objects.get(person=contact).email:
            return HttpResponse("<h1>You cannot delete a person who has phone or email</h1>")
        else:
            contact.delete()
            return redirect('contact-list')
    return render(request, "contacts/delete.html")

def search_view(request):
    querry = request.GET['q']
    querryset = querry.split(" ")
    print(querry)
    if len(querryset) > 1:
        if Person.objects.filter(first_name=querryset[0], last_name=querryset[1]):
            contacts = Person.objects.filter(first_name=querryset[0], last_name=querryset[1])
            for contact in contacts:
                try:
                    contact.phone = contact.phone_set.get(person=contact).phone
                    if contact.phone == None: contact.phone = ""
                    contact.email = contact.email_set.get(person=contact).email
                    if contact.email == None: contact.email = ""
                except Phone.DoesNotExist:
                    print("phone does not exist")
                except Email.DoesNotExist:
                    print("email does not exist")
    else:
        print("here!")
        if Person.objects.filter(first_name=querry):
            contacts = Person.objects.filter(first_name=querry)
            for contact in contacts:
                try:
                    contact.phone = contact.phone_set.get(person=contact).phone
                    if contact.phone == None: contact.phone = ""
                    contact.email = contact.email_set.get(person=contact).email
                    if contact.email == None: contact.email = ""
                except Phone.DoesNotExist:
                    print("phone does not exist")
                except Email.DoesNotExist:
                    print("email does not exist")
        elif Person.objects.filter(last_name=querry):
            contacts = Person.objects.filter(last_name=querry)
            for contact in contacts:
                try:
                    contact.phone = contact.phone_set.get(person=contact).phone
                    if contact.phone == None: contact.phone = ""
                    contact.email = contact.email_set.get(person=contact).email
                    if contact.email == None: contact.email = ""
                except Phone.DoesNotExist:
                    print("phone does not exist")
                except Email.DoesNotExist:
                    print("email does not exist")
        elif Phone.objects.filter(phone=querry):
            phones = Phone.objects.filter(phone=querry)
            contacts = []
            for element in phones:
                contacts.append(element.person)
            for contact in contacts:
                try:
                    contact.phone = contact.phone_set.get(person=contact).phone
                    if contact.phone == None: contact.phone = ""
                    contact.email = contact.email_set.get(person=contact).email
                    if contact.email == None: contact.email = ""
                except Phone.DoesNotExist:
                    print("phone does not exist")
                except Email.DoesNotExist:
                    print("email does not exist")
        elif Email.objects.filter(email=querry):
            emails = Email.objects.filter(email=querry)
            contacts = []
            for element in emails:
                contacts.append(element.person)
            for contact in contacts:
                try:
                    contact.phone = contact.phone_set.get(person=contact).phone
                    if contact.phone == None: contact.phone = ""
                    contact.email = contact.email_set.get(person=contact).email
                    if contact.email == None: contact.email = ""
                except Phone.DoesNotExist:
                    print("phone does not exist")
                except Email.DoesNotExist:
                    print("email does not exist")
        else:
            contacts = []

    context = {"contacts": contacts}
    return render(request, "contacts/list.html", context)
