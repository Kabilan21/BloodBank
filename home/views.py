from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib import messages
from .models import BloodData, BloodNeed
from django.http import JsonResponse


def register(request):
    blood_choice = []
    for each in BloodData.blood_choice:
        blood_choice.append(each[0])
    if request.method == 'POST':
        name = request.POST.get('name')
        DOB = request.POST.get('dob')
        email = request.POST.get('email')
        number = request.POST.get('number')
        bloodgroup = request.POST.get('bloodgroup')
        location = request.POST.get('location')
        receive_mail = request.POST.get('receive_mail')
        show_onsearch = request.POST.get('show_onsearch')
        more_location = request.POST.get('more_location')
        if receive_mail is None:
            receive_mail = False
        else:
            receive_mail = True
        if show_onsearch is None:
            show_onsearch = False
        else:
            show_onsearch = True
        bloodData = BloodData(name=name, DOB=DOB, email=email, number=number, bloodgroup=bloodgroup,
                              location=location, receive_mail=receive_mail, show_onsearch=show_onsearch, more_location=more_location)
        bloodData.save()
        messages.success(
            request, "Successfully registered.You can use your email id to update your profile or delete your profile.Thanks for taking a part in our programme.")

    return render(request, 'home/bloodregister.html', context={'blood_choice': blood_choice})


def bloodsearch(request):
    bloodgroup = request.POST.get('bloodgroup')
    location = request.POST.get('location')
    bloodData = BloodData.objects.filter(
        location__icontains=location, bloodgroup=bloodgroup)
    html_data = render_to_string(
        'home/bloodsearch.html', context={'donors': bloodData, 'length': len(bloodData)})
    return JsonResponse({'html_data': html_data})


def bloodprofile(request):
    if request.is_ajax and request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        bloodData = BloodData.objects.filter(email=email).first()
        if bloodData is None:
            return JsonResponse({'html_data': ' '})
        html_data = render_to_string(
            'home/bloodprofileupdate.html', context={'donor': bloodData})
        return JsonResponse({'html_data': html_data, 'bloodpk': bloodData.pk})
    return render(request, 'home/bloodprofile.html')


def profileupdate(request):
    if request.is_ajax and request.method == 'POST':
        operation = request.POST.get('operation')
        pk = request.POST.get('pk')
        bloodData = BloodData.objects.get(id=pk)
        if operation == 'update':
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            location = request.POST.get('location')
            receive_mail = request.POST.get('receive_mail')
            show_onsearch = request.POST.get('show_onsearch')
            more_location = request.POST.get('more_location')
            bloodData.name = name
            bloodData.email = email
            bloodData.number = number
            bloodData.location = location
            if receive_mail is None:
                receive_mail = False
            else:
                receive_mail = True
            if show_onsearch is None:
                show_onsearch = False
            else:
                show_onsearch = True
            bloodData.receive_mail = receive_mail
            bloodData.show_onsearch = show_onsearch
            bloodData.more_location = more_location
            bloodData.save()
            return JsonResponse({'status': 'Updated'})

        if operation == 'delete':
            bloodData.delete()
            return JsonResponse({'status': 'Deleted'})
    return JsonResponse({'status': 'Unknown'})


def bloodneed(request):
    blood_choice = []
    for each in BloodData.blood_choice:
        blood_choice.append(each[0])
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        attender_name = request.POST.get('attender_name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        bloodgroup = request.POST.get('bloodgroup')
        blood_units = request.POST.get('blood_units')
        location = request.POST.get('location')
        hospital_name = request.POST.get('hospital_name')
        can_afford_travel = request.POST.get('can_afford_travel')
        if can_afford_travel is None:
            can_afford_travel = False
        else:
            can_afford_travel = True
        bloodneed = BloodNeed(patient_name=patient_name, attender_name=attender_name, email=email, number=number, blood_units=blood_units,
                              bloodgroup=bloodgroup, location=location, hospital_name=hospital_name, can_afford_travel=can_afford_travel)
        bloodneed.save()
    return render(request, 'home/bloodneed.html', context={'blood_choice': blood_choice})


def bloodshare(request):
    blood_choice = []
    for each in BloodData.blood_choice:
        blood_choice.append(each[0])
    context = {'blood_choice': blood_choice,
               'blood_needs': BloodNeed.objects.all().order_by('-time_stamp')
               }
    return render(request, 'home/bloodhome.html', context=context)
