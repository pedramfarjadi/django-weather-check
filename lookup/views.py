from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=06938BC6-81EF-405A-AFA0-4DA5AA27E1D7")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."    

    #https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=06938BC6-81EF-405A-AFA0-4DA5AA27E1D7
    return render(request, 'home.html', {"api": api})

def about(request):
    return render(request, 'about.html', {})