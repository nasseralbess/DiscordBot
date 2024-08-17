import requests
weather = requests.get('https://api.open-meteo.com/v1/forecast',params={'latitude':32.02,'longitude':35.87,'daily':['temperature_2m_max','temperature_2m_min'],'timezone':'auto'})
import matplotlib.pyplot as plt
#format min temperature to be blue and max temperature to be red, add labels to the x and y axis, add legend
plt.xlabel('Time (days)')
plt.ylabel('Temperature (C)')
plt.legend(['Max Temperature','Min Temperature'])
plt.title('Temperature Forecast')
plt.plot(weather.json()['daily']['time'],weather.json()['daily']['temperature_2m_max'],'r')
plt.plot(weather.json()['daily']['time'],weather.json()['daily']['temperature_2m_min'],'b')
plt.grid()
#adding vertices
plt.legend(['Max Temperature','Min Temperature'])
#make the x axis labels more vertical for readability
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('weather.png')