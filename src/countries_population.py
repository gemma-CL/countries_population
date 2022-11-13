from collections import namedtuple
from datetime import datetime
import csv

Countries_Population = namedtuple('Countries_Population', 'Month, Year, Country, Population, Yearly_percentage_Change, Yearly_Change, Migrants_net, Median_Age, Fertility_Rate, Density_PKm2, Urban_Pop_percentage, Urban_Population, Countrys_Share_of_World_Pop_percentage, World_Population, Country_Global_Rank, War, Partner')


def lee_fichero(fichero):
    registros = []
    with open(fichero, encoding='utf-8', errors="ignore") as f:
     lector = csv.reader(f,delimiter=";")
     next(lector)
     for linea in lector:
        Month = int(linea[0])
        Year = int(linea[1])
        Country = str(linea[2])
        Population = int(linea[3])
        Yearly_percentage_Change = str(linea[4])
        Yearly_Change = int(linea[5])
        Migrants_net = int(linea[6])
        Median_Age = str(linea[7])
        Fertility_Rate = str(linea[8])
        Density_PKm2 = float(linea[9])
        Urban_Pop_percentage = str(linea[10])
        Urban_Population = str(linea[11])
        Countrys_Share_of_World_Pop_percentage = str(linea[12])
        World_Population = int(linea[13])
        Country_Global_Rank = int(linea[14])
        War = bool(linea[15])
        Partner = str(linea[16])
        #exact_date = parsea_date
        tupla = (Countries_Population(Month, Year, Country, Population, Yearly_percentage_Change, Yearly_Change, Migrants_net, Median_Age, Fertility_Rate, Density_PKm2, Urban_Pop_percentage, Urban_Population, Countrys_Share_of_World_Pop_percentage, World_Population, Country_Global_Rank, War, Partner))
        registros.append(tupla)
    return registros

def parsea_date(fecha):
    return datetime.strptime(fecha,'%Y-%M-%d').date()

def parsea_bool(War):
    '''Esto devuelve True si el país estuvo en guerra y false si no'''
    if War == "yes":
        return True
    else:
        return False

#BLOQUE 1

def calula_paises(registro):
    conjunto_paises = {r.Country for r in registro}
    return len(conjunto_paises)

def poblacion_pais_por_anyo(registro, years, pais):
    dato = [r.Population for r in registro if r.Year == years and r.Country == pais]
    result = dato
    return result

def media_poblacion_pais(registro, pais):
    result = [r.Population for r in registro if r.Country == pais]
    media = [sum(result)/len(result)]
    return media


#BLOQUE 2

def poblacion_mas_baja(registro):
    return min(registro, key=lambda x:x.Population).Country

def top_5_paises_mayor_poblacion(registro):
    result = sorted((r for r in registro if r.Country_Global_Rank <= 5))
    return result

def agrupa_por_paises(registro, pais):
    pais = 'China'
    claves = {r.Country for r in registro if r.Country == pais}
    dic = dict()
    for clave in claves:
        dic[clave] = [r.Population for r in registro if r.Country==clave]
    return dic

