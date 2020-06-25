#api3.geo.admin.ch

# headers = Taxon ID	Gruppe	Trivialname	Taxon	Gemeinde(n)	Kanton(e) 	Fundort	H�he	Koordx	Koordy	Radius	R�umliche Zusammenfassung	Anzahl	n Nachweise 	Jahr	Monat	Tag	Fortpflanzungsnachweis	Herkunft	Beobachter/Sammler	ID Beobachtung	Rote Liste	Priorit�t CH	UZL	WZL	Massnahmebedarf	Monitoring-Bedarf	NHV	SMARAGD	infoflora: Kantonaler Schutzstatus	infoflora: Rote Liste regional	Habitat	Substrat	swisslichens: Ecotyp	Ordnung	Familie	swissfungi: funktionelle Gruppe	Indigenat CH	Standortfremd	Einf�hrung
# Schweizer Koordinaten Bezugsystem = (LV95 CH1903+ / LV95 EPSG 2056)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

large = 22; med = 16; small = 12


"""
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)

"""


plant_data = pd.read_csv("MAR infoflora_200274_Pilatus.csv",sep=";", encoding="iso-8859-1", usecols=['Koordx', 'Koordy', 'Trivialname', 'Jahr'])
df = pd.DataFrame(plant_data)
print((df[df['Trivialname'] == 'Felsenmispel']))


x1 = []
y1 = []
x1 = df['Koordx'].to_list()
y1 = df['Koordy'].to_list()
name = df['Trivialname'].to_list()




plt.style.use('seaborn-whitegrid')
plt.xlabel('Koordx')
plt.ylabel('Koordy')
plt.title('Pilatus Pflanzen')


#Write a function which gets all plants where name = 

#plt.show()


