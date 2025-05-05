from django.shortcuts import render, HttpResponse
import joblib

model = joblib.load('static/random_forest_regressor')

# Create your views here.

def about(request):
    # return HttpResponse("This is the about page") 
    return render(request, 'about.html')



def prediction(request):
    # return HttpResponse("This is the prediction page")
    if request.method == "POST":
        # print("enter into the post request")
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))

        # print(age, bmi, sex, children, smoker, region)

        pred = round(model.predict([[age, sex, bmi, children, smoker, region]])[0])

        # print(pred)

        output = {
            "output": pred
        }

        return render(request, 'prediction.html', output)

    else:
        return render(request, 'prediction.html')

