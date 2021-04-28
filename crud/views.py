from django.shortcuts import render
from .models import Healthcare
# Create your views here.


def index(request):
    return render(request, 'index.html')


def emp(request):
    button = request.POST["b1"]
    if button == "Insert":
        name = request.POST["t2"]
        addr = request.POST["t3"]
        age = request.POST["t4"]
        gender = request.POST["gender"]
        group = request.POST["group"]
        try:
            Dentist = request.POST['Dentist']
        except:
            Dentist = 0
        try:
            Opthalmologist = request.POST['Opthalmologist']
        except:
            Opthalmologist = 0
        try:
            Orthopaedic = request.POST['Orthopaedic']
        except:
            Orthopaedic = 0
        dob = request.POST["dob"]
        total = request.POST["visits"]
        pic = (request.FILES["picture"])
        
        amount = request.POST["amount"]

        obj = Healthcare.objects.create(
            name=name, address=addr, age=age, gender=gender, group=group, dob=dob, total=total, pic=pic, amount=amount, Dentist=Dentist, Opthalmologist=Opthalmologist, Orthopaedic=Orthopaedic)

        msg = "Record Inserted"
        return render(request, 'result.html', {'msg': msg})

    elif button == "Select":
        id = request.POST['t1']
        obj = Healthcare.objects.get(pk=id)
        return render(request, 'result.html', {'obj': obj})

    elif button == "Update":

        id = request.POST["t1"]
        name = request.POST["t2"]
        addr = request.POST["t3"]
        age = request.POST["t4"]
        gender = request.POST["gender"]
        group = request.POST["group"]
        dob = request.POST["dob"]
        pic = (request.FILES["picture"])
        amount = request.POST["amount"]
        try:
            Dentist = request.POST['Dentist']
        except:
            Dentistt = 0
        try:
            Opthalmologist = request.POST['Opthalmologist']
        except:
            Opthalmologist = 0
        try:
            Orthopaedic = request.POST['Orthopaedic']
        except:
            Orthopaedic = 0

        obj = Healthcare.objects.get(pk=id)
        obj.name = name
        obj.address = addr
        obj.age = age
        obj.gender = gender
        obj.group = group
        obj.dob = dob
        obj.pic = pic
        obj.Dentist = Dentist
        obj.Opthalmologist = Opthalmologist
        obj.Orthopaedic = Orthopaedic

        obj.amount = amount

        obj.save()
        msg = "record updated"
        return render(request, 'result.html', {'msg': msg})

    elif button == "Delete":
        id = request.POST['t1']
        obj = Healthcare.objects.get(pk=id)
        obj.delete()
        msg = "record deleted"
        return render(request, 'result.html', {'msg': msg})
