

import pandas as pd
import matplotlib.pyplot as plt



unit = "kW"
name = "bus"
module_lib = "SandiaMod"
module = "Canadian_Solar_CS5P_220M___2009_"
inverter_lib = "cecinverter"
inverter = "Connect_Renewable_Energy__CE_4000__240V_"
surface_tilt = 20
surface_azimuth = 200
modules_per_string = 4
strings_per_inverter = 2
temp_lib = 'sapm'
temp_model = 'open_rack_glass_glass'
timebase = 15
charge_efficiency = 0.98
discharge_efficiency = 0.98
max_power = 4  
capacity = 4  
max_c = 1  
timestamp_int = 48
timestamp_str = "2021-06-01 12:00:00"


environment = Environment(timebase=timebase, start=start, end=end, year=year)
environment.get_pv_data(file=".csv")

user_profile = UserProfile(
    identifier=name, latitude=latitude, longitude=longitude
)

pv = Photovoltaic(
    unit=unit,
    identifier=(name + "_pv"),
    environment=environment,
    user_profile=user_profile,
    module_lib=module_lib,
    module=module,
    inverter_lib=inverter_lib,
    inverter=inverter,
    surface_tilt=surface_tilt,
    surface_azimuth=surface_azimuth,
    modules_per_string=modules_per_string,
    strings_per_inverter=strings_per_inverter,
    temp_lib=temp_lib,
    temp_model=temp_model
)

pv.prepare_time_series()

# StorageObj
storage = ElectricalEnergyStorage(
    unit=unit,
    identifier=(name + "_storage"),
    environment=environment,
    user_profile=user_profile,
    capacity=capacity,
    charge_efficiency=charge_efficiency,
    discharge_efficiency=discharge_efficiency,
    max_power=max_power,
    max_c=max_c,
)

baseload = pd.read_csv("./input/baseload/df_S_15min.csv")
baseload.drop(columns=["Time"], inplace=True)
baseload.set_index(environment.pv_data.index, inplace=True)

# baseLoad + PV_TimeSeries --> ResidualLoad
house_loadshape = pd.DataFrame(baseload["0"].loc[start:end] / 1000)
house_loadshape["PV_gen"] = pv.timeseries.loc[start:end]
house_loadshape["residualLoad"] = (
    baseload["0"].loc[start:end] / 1000 - pv.timeseries.bus_pv
)

storage.residual_load = house_loadshape.residual_load


def (storage):

    storage.prepare_time_series()
    print("TimeSeries:")
    print(storage.timeseries.head())
    storage.timeseries.plot(figsize=(16, 9))
    plt.show()


def (storage, timestamp):

    timestepvalue = storage.value_for_timestamp(timestamp)
    print("\nValForTimeStamp:\n", timestepvalue)


def (storage, timestamp):

    print("ObsForTimeStamp:")
    observation = storage.observations_for_timestamp(timestamp)
    print(observation, "\n")


def (storage, timestamp):

    print("opStorage:")
    state_of_charge, res_load = storage.operate_storage(
        storage.residual_load.loc[timestamp]
    )
    print("SOS: ", state_of_charge)
    print("residualLoad: ", res_load)

