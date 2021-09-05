from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    if request.method =="POST":
        zipcode =request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=06938BC6-81EF-405A-AFA0-4DA5AA27E1D7")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."    
        if api[0]['Category']['Name'] == "Good":   

            category_description = '(0 - 50) Air quality is considred satisfactory, and air pollution poses little or no risk.'
            category_color = "good"
                
        elif api[0]['Category']['Name'] == "Moderate": 
                
            category_description = '(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensetive to aire pollution.'
            category_color = "moderate"
            
        elif api[0]['Category']['Name'] == "Unhealthy for Sensetive Groups":   

            category_description = '(101 - 150) Although general public is not likly to be affected at this AQI range, people with lung disease, older adults and children are at greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children areat greater risk from the presence of particles in air.'
            category_color = "usg"
            
        elif api[0]['Category']['Name'] == "Unhealthy":    

            category_description = '(151 - 200) Everyone may begin to experience health effects; members off sensitive groups may experience serious health effects.'
            category_color = "unhealty"
            
        elif api[0]['Category']['Name'] == "Very Unhealthy":   

            category_description = '(201 - 300) Health alert: everyone may experience more serious health effects.'
            category_color = "veryunhealty"

        elif api[0]['Category']['Name'] == "Hazardous":    

            category_description = '(301 - 500) Health warnings of emergency conditions. the entire population ismore likely to be affected.'
            category_color = "hazardous"

        #https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=06938BC6-81EF-405A-AFA0-4DA5AA27E1D7
        return render(request, 'home.html', {
            "api": api,
            "category_description": category_description,
            "category_color": category_color
        })

    else:

        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10002&distance=25&API_KEY=06938BC6-81EF-405A-AFA0-4DA5AA27E1D7")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."    
        if api[0]['Category']['Name'] == "Good":   

            category_description = '(0 - 50) Air quality is considred satisfactory, and air pollution poses little or no risk.'
            category_color = "good"
                
        elif api[0]['Category']['Name'] == "Moderate": 
                
            category_description = '(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensetive to aire pollution.'
            category_color = "moderate"
            
        elif api[0]['Category']['Name'] == "Unhealthy for Sensetive Groups":   

            category_description = '(101 - 150) Although general public is not likly to be affected at this AQI range, people with lung disease, older adults and children are at greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children areat greater risk from the presence of particles in air.'
            category_color = "usg"
            
        elif api[0]['Category']['Name'] == "Unhealthy":    

            category_description = '(151 - 200) Everyone may begin to experience health effects; members off sensitive groups may experience serious health effects.'
            category_color = "unhealty"
            
        elif api[0]['Category']['Name'] == "Very Unhealthy":   

            category_description = '(201 - 300) Health alert: everyone may experience more serious health effects.'
            category_color = "veryunhealty"

        elif api[0]['Category']['Name'] == "Hazardous":    

            category_description = '(301 - 500) Health warnings of emergency conditions. the entire population ismore likely to be affected.'
            category_color = "hazardous"

        #https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=06938BC6-81EF-405A-AFA0-4DA5AA27E1D7
        return render(request, 'home.html', {
            "api": api,
            "category_description": category_description,
            "category_color": category_color
        })

def about(request):
    return render(request, 'about.html', {})