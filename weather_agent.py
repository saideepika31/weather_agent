{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a63752e-0a81-43d0-ba8c-bd58fa135f24",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "city_cordinates={\n",
    "    \"hyderabad\": {\"lat\": 17.3850, \"lon\": 78.4867},\n",
    "    \"mumbai\": {\"lat\": 19.0760, \"lon\": 72.8777},\n",
    "    \"delhi\": {\"lat\": 28.7041, \"lon\": 77.1025},\n",
    "    \"chennai\": {\"lat\": 13.0827, \"lon\": 80.2707},\n",
    "    \"bangalore\": {\"lat\": 12.9716, \"lon\": 77.5946}\n",
    "}\n",
    "def weather_city(cityname):\n",
    "    cityname=cityname.lower()\n",
    "    if cityname not in city_cordinates:\n",
    "        return \"no cityname detected\"\n",
    "\n",
    "    else:\n",
    "        lat=city_cordinates[cityname][\"lat\"]\n",
    "        lon=city_cordinates[cityname][\"lon\"]\n",
    "        url=f\"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true\"\n",
    "        response=requests.get(url)\n",
    "        data=response.json()\n",
    "\n",
    "        temp=data['current_weather']['temperature']\n",
    "        sped=data['current_weather']['windspeed']\n",
    "        \n",
    "        return f\"temperature of {cityname} is {temp} degrees and speed of wind is {sped} km/h \"        \n",
    "\n",
    "\n",
    "print(weather_city(\"hyderabad\"))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
