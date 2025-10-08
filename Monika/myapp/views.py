
from django.shortcuts import render
def calculate_BMI(request):
    BMI=None
    Weight=None
    Height=None
    if request.method == 'POST':
        print("POST method is used")
        Weight=float(request.POST.get("Weight"))
        Height=float(request.POST.get("Height"))/100
        BMI = Weight/(Height**2)
        BMI =round(BMI,2)
        print(f"1Weight in kg: {Weight} ,Height in m: {Height}, BMI: {BMI}")
    return render(request,'myapp/math.html',{'BMI':BMI})





