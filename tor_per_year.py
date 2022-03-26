import pandas as pd
import matplotlib.pyplot as plt

#read csv with tornado data
df=pd.read_csv("1950-2020_all_tornadoes.csv")  

#filter tornado data for tornadoes that occurred in march, april, or may
df=df.loc[(df['mo'] == 3) | (df['mo'] == 4) | (df['mo'] == 5)]

#Create series of total tornadoes (from mar/apr/may) per year
sr=df['yr'].value_counts()

#sort index, save indexes as year
sr=sr.sort_index()
year=sr.index[:]

#Create dictionary with years labeled by ENSO phase. Source: https://ggweather.com/enso/oni.htm
enso = {
   'weak_nina': [1955, 1965, 1972, 1975, 1984, 1985, 2001, 2006, 2009, 2017, 2018],
   'mod_nina': [1956, 1970, 1996, 2012],  #2021, 2022
   'strong_nina': [1950, 1974, 1976, 1989, 1999, 2000, 2008, 2011],
   'weak_nino': [1953, 1954, 1959, 1970, 1977, 1978, 1980, 2005, 2007, 2015, 2019],
   'mod_nino': [1952, 1964, 1968, 1987, 1995, 2003, 2010],
   'strong_nino': [1958, 1965, 1973, 1988, 1992],
   'vstrong_nino': [1983, 1998, 2016],
   'neutral':[1950, 1951, 1957, 1960, 1961, 1962, 1963, 1966, 1967, 1969, 1971, 1979, 1981, 1982, 1986, 1990, 1991, 1993, 1994, 2002, 2004, 2013, 2014, 2020]
}


#print the avg # of tornadoes per enso phase in the consolo
#print(sr[enso['weak_nina']].sum()/sr[enso['weak_nina']].count())
#print(sr[enso['mod_nina']].sum()/sr[enso['mod_nina']].count())
#print(sr[enso['strong_nina']].sum()/sr[enso['strong_nina']].count())
#print(sr[enso['weak_nino']].sum()/sr[enso['weak_nino']].count())
#print(sr[enso['mod_nino']].sum()/sr[enso['mod_nino']].count())
#print(sr[enso['strong_nino']].sum()/sr[enso['strong_nino']].count())
#print(sr[enso['vstrong_nino']].sum()/sr[enso['vstrong_nino']].count())
#print(sr[enso['neutral']].sum()/sr[enso['neutral']].count())


#Initialize list with 71 objects, each object is a string named 'gray'
colors=['gray']*71

#Replace the color in colors with the appropriate color based on the ENSO year
for yr in enso['neutral']:
    colors[yr-1950]='#E6E6E6'
for yr in enso['weak_nina']:
    colors[yr-1950]='#D3D3FC'
for yr in enso['mod_nina']:
    colors[yr-1950]='#7878FF'
for yr in enso['strong_nina']:
    colors[yr-1950]='#0000FF'
for yr in enso['weak_nino']:
    colors[yr-1950]='#FCD3D3'
for yr in enso['mod_nino']:
    colors[yr-1950]='#FF9595'
for yr in enso['strong_nino']:
    colors[yr-1950]='#FF3333'
for yr in enso['vstrong_nino']:
    colors[yr-1950]='maroon'


#create dictionary for the legend. Key = text to be shown in legend, value = color of legend entry
l = {
     'Strong La Nina Avg: 558': '#0000FF',
     'Moderate La Nina Avg: 355': '#7878FF',
     'Weak La Nina Avg: 440':'#D3D3FC',
     'Neutral Avg: 353': '#E6E6E6',
     'Weak El Nino Avg: 415': '#FCD3D3',
     'Moderate El Nino Avg: 395': '#FF9595',
     'Strong El Nino Avg: 312': '#FF3333',
     'Very Strong El Nino Avg: 470': 'maroon'
}         

#Plotting legend
labels = list(l.keys())
handles = [plt.Rectangle((0,0),1,1, color=l[label]) for label in labels]
plt.legend(handles, labels, fontsize=8)        

#Plot x axis title, y axis title, and chart title
plt.xlabel('Year')
plt.ylabel('Tornadoes')
plt.title('Mar-Apr-May US Tornadoes Per Year')
 
#make bar graph
graph=plt.bar(sr.index, sr, color = colors)

#show plot in console
plt.show()

#save plot
plt.savefig('tor_per_year.png', width=6, height=4, dpi=300)  
