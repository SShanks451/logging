import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import lasio
import sys
import json

json_data = sys.argv[1]

with open(json_data, "r") as file:
  x = file.read()
py_data = json.loads(x)
# print(py_data)

las=lasio.read("./las-file/well_data.las")

df = las.df()
# print(df)

dframe_gamma_ray = df["GR"]
# print(dframe_gamma_ray)

# gamma_ray_shale_value = 200
# gamma_ray_clean_value = 0

gamma_ray_shale_value = float(py_data["shale_value"])
gamma_ray_clean_value = float(py_data["clean_value"])

shale_volume_arr = []

def shale_volume(gamma_ray_log_value):
  return ((gamma_ray_log_value - gamma_ray_clean_value) / (gamma_ray_shale_value - gamma_ray_clean_value))

for val in dframe_gamma_ray:
  shale_volume_arr.append(shale_volume(val))

# print(shale_volume_arr)

df.reset_index(inplace=True)

y=df.DEPTH.values
dframe_depth = df["DEPTH"]

y_min = float(py_data["shallow_point"])
y_max = float(py_data["deep_point"])

dframe_shale_volume = shale_volume_arr


fig, ax3 = plt.subplots(1, 1, figsize=(3, 10))
curve_names = ['Shale Volume']


ax3.plot(dframe_shale_volume, df["DEPTH"], color="Black", lw=0.5)
ax3.set_xlim(0, 1)


ax3.spines['top'].set_edgecolor('Black')
ax3.set_ylim(y_max, y_min)
ax3.xaxis.set_ticks_position("top")
ax3.xaxis.set_label_position("top")
ax3.set_xlabel(curve_names[0])



ax3.grid()
ax3.axes.yaxis.set_ticklabels([])

plt.savefig('Shale_volume.png', bbox_inches='tight')

dframe_bulk_density = df["RHOB"]
# print(dframe_bulk_density)

# matrix_density_value = 2.65
# fluid_density_value = 1

matrix_density_value = float(py_data["matrix_density"])
fluid_density_value = float(py_data["fluid_density"])

density_porosity_arr = []

def density_porosity(bulk_density_log_value):
  return ((matrix_density_value-bulk_density_log_value) / (matrix_density_value  - fluid_density_value))
    
for val in dframe_bulk_density:
  density_porosity_arr.append(density_porosity(val))

# print(density_porosity_arr)

fig=plt.figure(figsize=(3,10))

x=density_porosity_arr
axes=fig.add_axes([0,0,1,1])
axes.plot(x,y, color = 'orange', lw=0.5)

axes.set_ylim(y_max, y_min) 
axes.set_xlim(0, 1)
axes.set_xlabel("Density Porosity")
axes.xaxis.set_label_position("top")
axes.xaxis.set_ticks_position("top")

axes.axes.yaxis.set_ticklabels([])

axes.set_xticks
axes.grid()
plt.savefig('Density_Porosity.png', bbox_inches='tight')

dframe_sonic_compressional = df["DTC"]
# print(dframe_sonic_compressional)

# fluid_transit_time_value = 189
# matrix_tansit_time_value = 55.5
# correction_factor_value = 1

fluid_transit_time_value = float(py_data["fluid_transit_time"])
matrix_tansit_time_value = float(py_data["matrix_transit_time"])
correction_factor_value = float(py_data["correction_factor_value"])

wylie_sonic_porosity_arr = []

def wylie_sonic_porosity(compressional_sonic_log_value):
  return ((compressional_sonic_log_value-matrix_tansit_time_value) / (fluid_transit_time_value  - matrix_tansit_time_value))
    
for val in dframe_sonic_compressional:
  wylie_sonic_porosity_arr.append(wylie_sonic_porosity(val))

# print(wylie_sonic_porosity_arr)

dframe_sonic_porosity = wylie_sonic_porosity_arr


fig, ax3 = plt.subplots(1, 1, figsize=(3, 10))
curve_names = ['Sonic Porosity']


ax3.plot(dframe_sonic_porosity, df["DEPTH"], color="magenta", lw=0.5)
ax3.set_xlim(0, 1)


ax3.spines['top'].set_edgecolor('magenta')
ax3.set_ylim(y_max, y_min)
ax3.xaxis.set_ticks_position("top")
ax3.xaxis.set_label_position("top")
ax3.set_xlabel(curve_names[0])



ax3.grid()
ax3.axes.yaxis.set_ticklabels([])
plt.savefig('Sonic_Porosity.png', bbox_inches='tight')

# import numpy as np

# def subtract_arrays(arr1, arr2):
#     # Convert lists to NumPy arrays
#     np_arr1 = np.array(arr1)
#     np_arr2 = np.array(arr2)
    
#     # Perform element-wise subtraction
#     result = np_arr1 - np_arr2
    
#     return result

# # Example usage:
# arr1 = dframe_neutron_porosity
# arr2 = density_porosity_arr

# result_array = subtract_arrays(arr1, arr2)
# print(result_array)

# plt.plot(result_array)

dframe_neutron_porosity = df["NPHI"]
# print(dframe_neutron_porosity)

fig=plt.figure(figsize=(3,10))

x = dframe_neutron_porosity
axes=fig.add_axes([0,0,1,1])
axes.plot(x,y, color = 'red', lw=0.5)

axes.set_ylim(y_max, y_min)
axes.set_xlim(0, 1)
axes.set_xlabel("Neutron Porosity")
axes.xaxis.set_label_position("top")
axes.xaxis.set_ticks_position("top")

axes.axes.yaxis.set_ticklabels([])

axes.set_xticks
axes.grid()
plt.savefig('Neutron_Porosity.png', bbox_inches='tight')

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd

import pandas as pd


data_array = [density_porosity_arr]

transposed_array = list(map(list, zip(*data_array)))


column_names = ['Density Porosity']

# Create DataFrame from transposed array
df_Density_porosity = pd.DataFrame(transposed_array, columns=column_names)

# # Create DataFrame from array
# df_Density_porosity = pd.DataFrame(data_array, columns=column_names)

# Display the DataFrame
# print(df_Density_porosity)

fig, ax3 = plt.subplots(1, 1, figsize=(3, 10))


curve_names = ['Density Porosity', 'Neutron Porosity']

ax4 = ax3.twiny()

ax3.plot(df_Density_porosity["Density Porosity"], df["DEPTH"], color="green", lw=0.5)
ax3.set_xlim(0, 1)
ax3.spines['top'].set_edgecolor('green')

ax4.plot(df["NPHI"], df["DEPTH"], color="orange", lw=0.5)
ax4.set_xlim(0, 1)
ax4.spines['top'].set_edgecolor('orange')

ax3.set_ylim(y_max, y_min)
ax3.xaxis.set_ticks_position("top")
ax3.xaxis.set_label_position("top")
ax3.xaxis.set_major_locator(MultipleLocator(0.2))
ax3.set_xlabel(curve_names[0])
ax3.grid()

ax4.set_ylim(y_max, y_min)
ax4.xaxis.set_major_locator(MultipleLocator(0.2))
ax4.xaxis.set_ticks_position("top")
ax4.xaxis.set_label_position("top")
ax4.set_xlabel(curve_names[1])
ax4.spines['top'].set_position(('axes', 1.08))

ax3.axes.yaxis.set_ticklabels([])
ax4.axes.yaxis.set_ticklabels([])

plt.savefig('Neutron_Porosity_Density_Porosity.png', bbox_inches='tight')

import numpy as np

def rms_of_porosity(arr1, arr2):
  # Convert lists to NumPy arrays
  np_arr1 = np.array(arr1)
  np_arr2 = np.array(arr2)
    
  # Calculate RMS element-wise
  rms_result = np.sqrt((np_arr1**2 + np_arr2**2) / 2)
    
  return rms_result

# Example usage:
arr1 = dframe_neutron_porosity
arr2 = density_porosity_arr

rms_array = rms_of_porosity(arr1, arr2)
# print("Root Mean Square of Porosiy:", rms_array)

dframe_true_resistivity_formation = df["RT"]
# print(dframe_true_resistivity_formation)

import numpy as np
Rt_array = dframe_true_resistivity_formation
def calculate_water_saturation(Rw, Rt_array, porosity_array, a, m, n):
    # Calculate water saturation using Archie's equation
    water_saturation = ((a * Rw) / (Rt_array * porosity_array ** m)) ** (1 / n)
    return water_saturation
porosity_array = rms_array

Rw = float(py_data["true_formation_resistivity"])

porosity_array = rms_array

a = float(py_data["tortuosity"])
m = float(py_data["cementation_exponent"])
n = float(py_data["saturation_exponent"])

# Calculate water saturation
water_saturation_array = calculate_water_saturation(Rw, Rt_array, porosity_array, a, m, n)
# print("Water Saturation Array:", water_saturation_array)

# print(len(y))

dframe_water_saturation = water_saturation_array


fig, ax3 = plt.subplots(1, 1, figsize=(3, 10))
curve_names = ['Water Saturation']


ax3.plot(dframe_water_saturation, df["DEPTH"], color="Blue", lw=0.5)
ax3.set_xlim(0, 1)


ax3.spines['top'].set_edgecolor('Green')
ax3.set_ylim(y_max, y_min)
ax3.xaxis.set_ticks_position("top")
ax3.xaxis.set_label_position("top")
ax3.set_xlabel(curve_names[0])

ax3.fill_betweenx(df["DEPTH"], dframe_water_saturation, color='cyan')

ax3.grid()
ax3.axes.yaxis.set_ticklabels([])
plt.savefig('SwArch.png', bbox_inches='tight')

# dframe_callipar_log = df["CALI"]
# print(dframe_callipar_log)


# fig=plt.figure(figsize=(3,10))

# x = dframe_callipar_log
# axes=fig.add_axes([0,0,1,1])
# axes.plot(x,y, color = 'black', lw=0.5)

# axes.set_ylim(y_max, y_min) 
# axes.set_xlim(0, 20)
# axes.set_xlabel("Callipar Log")
# axes.xaxis.set_label_position("top")
# axes.xaxis.set_ticks_position("top")

# axes.set_xticks
# axes.grid()
# plt.show()

# dframe_callipar_log = df["BS"]
# print(dframe_callipar_log)


# fig=plt.figure(figsize=(3,10))

# x = dframe_callipar_log
# axes=fig.add_axes([0,0,1,1])
# axes.plot(x,y, color = 'black', lw=0.5)

# axes.set_ylim(y_max, y_min) 
# axes.set_xlim(0, 20)
# axes.set_xlabel("Bore Hole Size")
# axes.xaxis.set_label_position("top")
# axes.xaxis.set_ticks_position("top")

# axes.set_xticks
# axes.grid()
# plt.show()

# dframe_gamma_ray_log = df["GR"]
# # print(dframe_gamma_ray_log)


# fig=plt.figure(figsize=(3,10))

# x = dframe_gamma_ray_log
# axes=fig.add_axes([0,0,1,1])
# axes.plot(x,y, color = 'Red', lw=0.5)

# axes.set_ylim(y_max, y_min) 
# axes.set_xlim(0, 200)
# axes.set_xlabel("Gamma Ray")
# axes.xaxis.set_label_position("top")
# axes.xaxis.set_ticks_position("top")

# axes.set_xticks
# axes.grid()

# axes.axes.yaxis.set_ticklabels([])


# plt.savefig('Gaa.png', bbox_inches='tight')
# # plt.show()

# import matplotlib.pyplot as plt
# from matplotlib.ticker import MultipleLocator
# import pandas as pd



# fig, ax3 = plt.subplots(1, 1, figsize=(3, 10))


# curve_names = ['Gamma', 'Calliper']

# ax4 = ax3.twiny()

# ax3.plot(df["GR"], df["DEPTH"], color="pink", lw=0.5)
# ax3.set_xlim(0 ,200)
# ax3.spines['top'].set_edgecolor('pink')

# ax4.plot(df["CALI"], df["DEPTH"], color="black", lw=0.5)
# ax4.set_xlim(0, 10)
# ax4.spines['top'].set_edgecolor('black')

# ax3.set_ylim(y_max, y_min)
# ax3.xaxis.set_ticks_position("top")
# ax3.xaxis.set_label_position("top")
# ax3.xaxis.set_major_locator(MultipleLocator(20))
# ax3.set_xlabel(curve_names[0])
# ax3.grid()

# ax4.set_ylim(y_max, y_min)
# ax4.xaxis.set_major_locator(MultipleLocator(1))
# ax4.xaxis.set_ticks_position("top")
# ax4.xaxis.set_label_position("top")
# ax4.set_xlabel(curve_names[1])
# ax4.spines['top'].set_position(('axes', 1.08))

# plt.show()

dframe_deep_resistivity_log = df["RT"]
# print(dframe_deep_resistivity_log)


fig, ax3 = plt.subplots(1, 1, figsize=(3, 10))
curve_names = ['Deep Resistivity']


ax3.plot(df["RT"], df["DEPTH"], color="Green", lw=0.5)
ax3.set_xlim(0.2, 1000)

ax3.semilogx()
ax3.spines['top'].set_edgecolor('Green')
ax3.set_ylim(y_max, y_min)
ax3.xaxis.set_ticks_position("top")
ax3.xaxis.set_label_position("top")
ax3.set_xlabel(curve_names[0])

ax3.grid()
ax3.axes.yaxis.set_ticklabels([])
plt.savefig('Deep_Res.png', bbox_inches='tight')

fig, ax3 = plt.subplots(1, 1, figsize=(3, 10))


curve_names = ['Density', 'Neutron']

ax4 = ax3.twiny()

ax3.plot(df["RHOB"], df["DEPTH"], color="red", lw=0.5)
ax3.set_xlim(1.95, 2.95)
ax3.spines['top'].set_edgecolor('red')

ax4.plot(df["NPHI"], df["DEPTH"], color="blue", lw=0.5)
ax4.set_xlim(0.45, -0.15)
ax4.spines['top'].set_edgecolor('blue')

ax3.set_ylim(y_max, y_min)
ax3.xaxis.set_ticks_position("top")
ax3.xaxis.set_label_position("top")
ax3.set_xlabel(curve_names[0])
ax3.grid()

ax4.set_ylim(y_max, y_min)
ax4.xaxis.set_major_locator(MultipleLocator(0.1))
ax4.xaxis.set_ticks_position("top")
ax4.xaxis.set_label_position("top")
ax4.set_xlabel(curve_names[1])
ax4.spines['top'].set_position(('axes', 1.08))

ax3.axes.yaxis.set_ticklabels([])
ax4.axes.yaxis.set_ticklabels([])

plt.savefig('Neutron_Density.png', bbox_inches='tight')

fig, ax3 = plt.subplots(1, 1, figsize=(3, 10))


curve_names = ['Compressional', 'Shear']

ax4 = ax3.twiny()

ax3.plot(df["DTC"], df["DEPTH"], color="pink", lw=0.5)
ax3.set_xlim(240, 40)
ax3.spines['top'].set_edgecolor('pink')

ax4.plot(df["DTS"], df["DEPTH"], color="black", lw=0.5)
ax4.set_xlim(240, 40)
ax4.spines['top'].set_edgecolor('black')

ax3.set_ylim(y_max, y_min)
ax3.xaxis.set_ticks_position("top")
ax3.xaxis.set_label_position("top")
ax3.xaxis.set_major_locator(MultipleLocator(40))
ax3.set_xlabel(curve_names[0])
ax3.grid()

ax4.set_ylim(y_max, y_min)
ax4.xaxis.set_major_locator(MultipleLocator(40))
ax4.xaxis.set_ticks_position("top")
ax4.xaxis.set_label_position("top")
ax4.set_xlabel(curve_names[1])
ax4.spines['top'].set_position(('axes', 1.08))

ax3.axes.yaxis.set_ticklabels([])
ax4.axes.yaxis.set_ticklabels([])

plt.savefig('Shear_Compressional.png', bbox_inches='tight')

fig, ax3 = plt.subplots(1, 1, figsize=(3, 10))


curve_names = ['Calliper Log', 'Borehole Size', 'Gamma Ray Log']

ax4 = ax3.twiny()
ax5 = ax3.twiny()

ax3.plot(df["CALI"], df["DEPTH"], color="Brown", lw=0.5)
ax3.set_xlim(0, 15)
ax3.spines['top'].set_edgecolor('Brown')

ax4.plot(df["BS"], df["DEPTH"], color="black", lw=0.5)
ax4.set_xlim(0, 15)
ax4.spines['top'].set_edgecolor('black')

ax5.plot(df["GR"], df["DEPTH"], color="REd", lw=0.5)
ax5.set_xlim(0, 200)
ax5.spines['top'].set_edgecolor('Red')

ax3.set_ylim(y_max, y_min)
ax3.xaxis.set_ticks_position("top")
ax3.xaxis.set_label_position("top")
ax3.xaxis.set_major_locator(MultipleLocator(3))
ax3.set_xlabel(curve_names[0])
ax3.grid()

ax4.set_ylim(y_max, y_min)
ax4.xaxis.set_major_locator(MultipleLocator(3))
ax4.xaxis.set_ticks_position("top")
ax4.xaxis.set_label_position("top")
ax4.set_xlabel(curve_names[1])
ax4.spines['top'].set_position(('axes', 1.08))

ax5.set_ylim(y_max, y_min)
ax5.xaxis.set_major_locator(MultipleLocator(40))
ax5.xaxis.set_ticks_position("top")
ax5.xaxis.set_label_position("top")
ax5.set_xlabel(curve_names[2])
ax5.spines['top'].set_position(('axes', 1.16))

plt.savefig('Gamma_ray_log_borehole_size_calliper_log.png', bbox_inches='tight')

column_names = ['Depth', 'Shale Volume', 'Density Porosity', 'Sonic Porosity', 'Water Saturation']

# Create DataFrame from arrays
df = pd.DataFrame({
    'Depth': dframe_depth,
    'Shale Volume': shale_volume_arr,
    'Density Porosity': density_porosity_arr,
    'Sonic Porosity': wylie_sonic_porosity_arr,
    'Water Saturation': water_saturation_array
})

# Create DataFrame from the dictionary
# df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('Calculations.xlsx', index=False)

print("CHILD TASK FINISHED")