
import matplotlib.pyplot as plt

from pPa_Lib.environment import Environment
from pPa_Lib.wind_power import WindPower


start = "2021-01-01 00:00:00"
end = "2021-01-31 23:45:00"
timezone = ""
timestamp_int = 12
timestamp_str = "2015-01-01 12:00:00"

environment = Environment(start=start, end=end, timezone=timezone)

environment.get_wind_data(
    file="./input/wind/dwd_wind_data_2015.csv", utc=False
)

turbine_type = "E-126/4200"
hub_height = 135
rotor_diameter = 127
fetch_curve = "power_curve"
data_source = "oedb"


wind_speed_model = "logarithmic"
density_model = "ideal_gas"
temperature_model = "linear_gradient"
power_output_model = "power_coefficient_curve"  
density_correction = True
obstacle_height = 0
hellman_exp = None

wind = WindPower(
    unit="kW",
    identifier=None,
    environment=environment,
    user_profile=None,
    turbine_type=turbine_type,
    hub_height=hub_height,
    rotor_diameter=rotor_diameter,
    fetch_curve=fetch_curve,
    data_source=data_source,
    wind_speed_model=wind_speed_model,
    density_model=density_model,
    temperature_model=temperature_model,
    power_output_model=power_output_model,
    density_correction=density_correction,
    obstacle_height=obstacle_height,
    hellman_exp=hellman_exp,
)


def prepTimeSeries(wind):

    wind.prepare_time_series()
    print(wind.timeseries.head())
    wind.timeseries.plot(figsize=(16, 9))
    plt.show()


def tstValForTimestamp(wind, timestamp):

    timestepvalue = wind.value_for_timestamp(timestamp)
    print("\n valForTimeStamp:\n", timestepvalue)


def obsForTimesStamp(wind, timestamp):

    print("observations_for_timestamp:")
    observation = wind.observations_for_timestamp(timestamp)
    print(observation, "\n")


test_prepare_time_series(wind)
test_value_for_timestamp(wind, timestamp_int)
test_value_for_timestamp(wind, timestamp_str)

observations_for_timestamp(wind, timestamp_int)
observations_for_timestamp(wind, timestamp_str)
