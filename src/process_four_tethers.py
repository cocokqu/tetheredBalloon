''' imports '''
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# loading the file
year = 2026
month = 06
day = 10
hour = 11
minute = 42
timestamp = datetime(year, month, day, hour, minute,)

file_name = f"tether_data_{timestamp}.csv"
df = pd.read_csv('data.csv')

# calibration
# Replace these with the values printed by calibrate_one_tether.py
offset = 84321.0
scale = 0.0011160409

df["T1_N"] = (df["raw1"] - offset) * scale




# constants
c_drag = 0.1
r = 0.25
velocity = 15
mass = 50/1000
g = 9.8
rho_air = 1.225
rho_helium = 0.179
mu = 0.0000181
# mu is dynamic viscosity of air
# theta is angle from vertical downward direction
# beta is angle in horizontal plane
theta = 0
beta1 = 0
beta2 = math.pi/2
beta3 = math.pi
beta4 = 3 * math.pi/2
# Lengths of tethers
L1 = 0
L2 = 0
L3 = 0
L4 = 0

# first, calculating buoyancy, and lift

volume = (4/3) * math.pi * r**3
m_helium = rho_helium * volume
# Solving buoyancy and weight
f_buoyancy = (rho_air) * g * volume
# add mass of helium
f_weight = (mass + m_helium) * g
# add lift
f_lift = np.array([[0], [0], [f_buoyancy - f_weight]])


# vectorizing tension
vector_df = pd.dataFrame(
    columns=[
        'time_ms',
        'T1_x', 'T1_y', 'T1_z',
        'T2_x', 'T2_y', 'T2_z',
        'T3_x', 'T3_y', 'T3_z',
        'T4_x', 'T4_y', 'T4_z'
    ])

# helper function to turn a tension into a vector
def tension_vector(T, theta, beta):
    ''' vectorizes measured tension '''
    T_vec = np.array([
        [T * math.sin(theta) * math.cos(beta)],
        [T * math.sin(theta) * math.sin(beta)],
        [-T * math.cos(theta)]
    ])

    return T_vec

# takes in the original df
# outputs new df with tensions vectorized
def tension_dataframe(df):
    for x, row in df.iterrows():
        T1 = row['T1']
        T2 = row['T2']
        T3 = row['T3']
        T4 = row['T4']

        T1_vec = tension_vector(T1, theta, beta1)
        T2_vec = tension_vector(T2, theta, beta2)
        T3_vec = tension_vector(T3, theta, beta3)
        T4_vec = tension_vector(T4, theta, beta4)

        time = row['time_ms']

        vector_df.loc[len(vectir_df)] = [
            time,
            T1_vec[0], T1_vec[1], T1_vec[2],
            T2_vec[0], T2_vec[1], T2_vec[2],
            T3_vec[0], T3_vec[1], T3_vec[2],
            T4_vec[0], T4_vec[1], T4_vec[2]
        ]

    return vector_df


    # creates a dataframe of drag vectors with time
    def drag_vector(T, theta, beta):
        ''' vectorizes measured drag '''
