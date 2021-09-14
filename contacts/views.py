from datetime import datetime
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
from django.shortcuts import redirect, render

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        user_id = request.POST ['user_id']
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id = listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already sent an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(name=name,listing_id=listing_id,listing=listing,
        user_id=user_id,email=email,phone=phone,message=message)
        contact.save()
        send_mail(
            'Property ' +listing+' inquiry',
            'There has been an inquiry for '+listing+'. For more information check admin panel.',
            'kashefirojina8@gmail.com',
            [realtor_email,'rojina.kashefi@yahoo.com'],
            fail_silently=False

        )
        messages.success(request,'Your request has been submited your realtor will call you as soon as possible')
        return redirect('/listings/'+listing_id)