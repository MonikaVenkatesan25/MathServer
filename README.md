# Ex.05 Design a Website for Server Side Processing
## Date:08.10.2025

## AIM:
 To design a website to calculate the Body Mass Index (BMI) in the server side. 


## FORMULA:
BMI = W/H<sup>2</sup>
<br> BMI --> Body Mass Index 
<br> w --> weight
<br> H --> Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
<html>
<title>Body Mass Index</title>
<style>
body
{
background-color:rgb(9, 172, 242);
}
.edge {
width: 1650px;
margin-left: auto;
margin-right: auto;
padding-top: 400px;
padding-left: 350px;
}
.box {
display:block;
border: solid 7px peru;
width: 800px;
min-height: 400px;
font-size: 50px;
background-color: rgb(255, 121, 255);
}
.formelt{
color:dark black(134, 25, 217);
text-align: center;
margin-top: 7px;
margin-bottom: 7px;
}
</style>
</head>
<body>
<div class= "edge">
<div class= "box">
<h1 align="center">Body Mass Index</h1>
<h3 align="center">MONIKA V (25017555)</h3>
<form method="POST">
{% csrf_token %}
<div class= "formelt">
Weight: <input type= "text" name="Weight" value="{{Weight}}"></input>(in kg)<br/>
</div>
<div class= "formelt"> 
Height: <input type="text" name="Height" value="{{Height}}"></input>(in m)<br/>
</div>
<div class= "formelt">
<input type="submit" value="Calculate"><br/>
</div>
<div class= "formelt">
BMI: <input type="text" name="BMI" value="{{BMI}}" align:"center"></input>kg/m<sup>3</sup><br/>
</div>
</form>
</div>
</div>
</body>
</html>


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

    from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculate_BMI,name="home"),
    path('bmi/', views.calculate_BMI,name='bmi')
]




```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot (37).png>)


## HOMEPAGE:
![alt text](<Screenshot (35).png>)



## RESULT:
The program for performing server side processing is completed successfully.
