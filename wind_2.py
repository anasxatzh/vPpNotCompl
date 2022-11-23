

import matplotlib.pyplot as plt




environment = Environment(start=start, end=end, timezone=timezone)

environment.get_wind_data(
    file=".csv", utc=False
)

# WindTurbineData
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


def (wind):

    wind.prepare_time_series()
    wind.timeseries.plot(figsize=(16, 9))
    plt.show()

def (wind, timestamp):

    timestepvalue = wind.value_for_timestamp(timestamp)


def (wind, timestamp):

    observation = wind.observations_for_timestamp(timestamp)


