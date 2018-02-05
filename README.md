# Weather data generator

This script generates weather data for various cities around the world. The file `GlobalAirportDatabase.txt` contains IATA codes,
latitude, longitude and altitude information for various airports around the world. The parameters in constants.py determine
what cities to generate the data for, and what dates to generate the data for.

`weather_models.py` contains the weather model for each city. The temperature, pressure and relative humidity are modelled as
normal distributions within each month of the year. The generated values are adjusted according to the conditions for that day
based on the `adjust` parameter of the model. The conditions (`Overcast`, `Rain`, `Snow`, `Sunny`) are randomly 
generated based on the `condition_weights` for each city.

# Running the script

``` time python generate_weather.py ``` outputs to stdout the generated weather data. On my machine, it takes around 
1.5 seconds generate data for 10 cities over 11 years.

The script can be further parallelized by increasing the number of processors available on the host, and setting the 
python multiprocessing.Pool's processors to a higher value.
