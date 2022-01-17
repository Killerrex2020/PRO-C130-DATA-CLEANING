import pandas as pd
import csv

df = pd.read_csv('final.csv')
print(df.shape)
del df["hyperlink"]
del df["temp_planet_mass"]
del df["temp_planet_date"]
del df["pl_letter"]
del df["pl_name"]
del df["pl_pnum"]
del df["gaia_gmagerr"]
del df["gaia_gmaglim"]
del df["st_tefferr2"]
del df["st_mass"]

df = df.rename({
                'pl_hostname':"solar_system_name",
                'st_mass':"host_mass",
                'st_rad':"host_radius",
                'st_teff':"host_temperature"
},axis='columns')
df.to_csv('pagalhojao.csv')
print(df.shape)