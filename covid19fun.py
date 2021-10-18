import requests


response = requests.get("https://covid-api.mmediagroup.fr/v1/cases", verify=False)
list={}
list2={}
list3={}

alldata= response.json()
countrylist=alldata.keys()

for country in countrylist:
    confirmed=(alldata[country]["All"]["confirmed"])
    list3[confirmed]=country
    try:
        sq=(alldata[country]["All"]["sq_km_area"])
    except:
        sq=0
    try:
        pop=(alldata[country]["All"]["population"])
    except:
        pop=0
    if pop!=0:
        list[country]=confirmed/pop
    if sq!=0:
        list2[country]=sq/100
    
confirmedco= sorted(list3.items(), reverse=True )
a = sorted(list.items(), key=lambda x: x[1])
print("First 5 Countries with the most confirmes by capita")
print(a[:5])
print("This Average confirmes cases per 100 squre by country")
print(list2)
print("top 10 countries")
print(confirmedco[:10])

