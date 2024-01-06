from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Detail
import json

# Create your views here.
# def Home(request):
#     return render(request,"home1.html")

def Ajexdata(request):
    if request.method == "POST":
        sid = request.POST.get("stuid")
        print(sid)
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        if(sid == ""):
            obj = Detail.objects.create(name=name, email=email, phone=phone)
            obj.save()
        else:
            obj = Detail.objects.get(id=sid)
            obj.name = name
            obj.email = email
            obj.phone = phone
            obj.save()
        show = Detail.objects.values()
        alldata = list(show)
        response_data = {
            "message": "Save",
            "alldata": alldata
        }
        return JsonResponse(response_data)

    return JsonResponse({"message": "Invalid request"}, status=400)

# def Showalldata(request):
#     details = Detail.objects.all()
#     data1 = [{'name': detail.name, 'email': detail.email, 'phone': detail.phone} for detail in details]
#     print(data1)
#     ab = json.dumps(data1)  # Use json.dumps to convert data1 to a JSON string
#     return HttpResponse('ab') 

def Showalldata(request):
    deatil1=Detail.objects.all()
    return render(request,"home1.html",{'deatil1':deatil1})


def Deletedata(request):
   if request.method == "POST":
       data = json.loads(request.body)
       id = data.get('sid')
       print(id)
       pi = Detail.objects.get(pk=id)
       pi.delete()
       print('manish')
       return JsonResponse({"message": "Delete"})



def Editdata(request):
   if request.method == "POST":
       data1 = json.loads(request.body)
       print(data1)
       id1 = data1.get('sid')
       print(id1)
       edit1 = Detail.objects.get(pk=id1)
       editdata={"message": "edit", "id": edit1.id ,"name":edit1.name,"email":edit1.email,"phone":edit1.phone}
       return JsonResponse(editdata)