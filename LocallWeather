import requests

class LocalWeather:
    geodata, weatherdata = None, None

    #Get our IP for Geoloc purposes
    def getIP(self):
        return requests.get('http://get.geojs.io/v1/ip.json').json()['ip']

    #Set GeoData so we know where we are
    def setGeoData(self, myip):
        self.geodata = requests.get('https://get.geojs.io/v1/ip/geo/{0}.json'.format(myip)).json()

    #Get Location of Weather data from Weather API
    def setWeatherData(self):
        self.weatherdata = requests.get(f'https://api.weather.gov/points/{self.geodata["latitude"]},{self.geodata["longitude"]}').json()

    #Get Hourly forecast data
    def getLocalWeather(self):
        return requests.get(self.weatherdata['properties']['forecastHourly']).json()

    #Iterates through forecast data from now until n hours from now
    def getHourly(self, hours):
        k = 0;
        hourlyResults = []
        localweather = self.getLocalWeather()['properties']['periods']
        
        for i in localweather:
            if k>hours:
                return hourlyResults
            hourlyResults.append(i)
            k+=1

    def __init__(self):
        self.setGeoData(self.getIP())
        self.setWeatherData()


weather = LocalWeather()
hourlyForecast = weather.getHourly(7)

k = 0

print(f'Current weather in {weather.geodata["city"]}')
for i in hourlyForecast:
    print(f'+{k}:00hrs | {i["temperature"]} deg-F')
    k+=1
