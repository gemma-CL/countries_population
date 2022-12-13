from collections import namedtuple, defaultdict
from datetime import datetime
import csv
from matplotlib import pylab as plt


Countries_Population = namedtuple('Countries_Population', 'Month, Year, Country, Population, Yearly_percentage_Change, Yearly_Change, Migrants_net, Median_Age, Fertility_Rate, Density_PKm2, Urban_Pop_percentage, Urban_Population, Countrys_Share_of_World_Pop_percentage, World_Population, Country_Global_Rank, War, Partner, date')


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
        date = parsea_date
        tupla = (Countries_Population(Month, Year, Country, Population, Yearly_percentage_Change, Yearly_Change, Migrants_net, Median_Age, Fertility_Rate, Density_PKm2, Urban_Pop_percentage, Urban_Population, Countrys_Share_of_World_Pop_percentage, World_Population, Country_Global_Rank, War, Partner, date))
        registros.append(tupla)
    return registros

def parsea_date(date):
    return datetime.strptime(date,"%d/%m/%Y").date()

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
    claves = {r.Country for r in registro}
    dic = dict()
    for clave in claves:
        dic[clave] = [r.Population for r in registro]
    result = sorted(dic.keys(), key = lambda x:x[1])[:5]
    return result

def agrupa_por_paises(registro, pais):
    claves = {r.Country for r in registro if r.Country == pais}
    dic = dict()
    for clave in claves:
        dic[clave] = [r.Population for r in registro if r.Country==clave]
    return dic



#BLOQUE 3
#Función 2
def total_migrantes_pais(registro, pais):
    claves = {r.Country for r in registro if r.Country == pais}
    dic = dict()
    for clave in claves:
        dic[clave] = [r.Migrants_net for r in registro if r.Country == clave]
    #result = sorted(dic.values())
    #total = sum(result)
    return dic

def total_migrantes_paisD(registro, pais):
    result = defaultdict(int)
    for r in registro:
        if r.Country == pais:
            result[r.Country] += r.Migrants_net
    return result

#Función 3
def pais_menor_fertilidad_anyo(registro, year):
    claves = {r.Country for r in registro if r.Year == year}
    dic = dict()
    for clave in claves:
        dic[clave] = [r.Fertility_Rate for r in registro if r.Year == clave ]
    result = sorted(dic.keys(), key = lambda x:x[1])[:1]
    return result

#Función 5
def mayor_porcentaje_pop_urbana(registro, pais):
    claves = {r.Country for r in registro if r.Country == pais}
    dic = dict()
    for clave in claves:
        dic[clave] = [r.Urban_Pop_percentage for r in registro if r.Country == clave]
    result = max(sorted(dic.values()), key = lambda x:x[1])[:1]
    return result

#Función 7
def top_7_paises_densidad_km2_anyo(registro,year):
    claves = {r.Country for r in registro if r.Year == year}
    dic = dict()
    for clave in claves:
        dic[clave] = [r.Density_PKm2 for r in registro if r.Year == clave]
    result = sorted(dic.keys(), key = lambda x:x[1])[:7]
    return result

#BLOQUE 4
def grafica(etiquetas, valores, titulo, etiqueta_x, etiqueta_y):
    plt.title(titulo)
    indice = range(len(etiquetas))
    plt.bar(indice, valores)
    plt.xticks(indice, etiquetas, fontsize = 8)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.show()

def population_country(registro, pais):
    claves = {r.Year for r in registro if r.Country == pais}
    dic = dict()
    for clave in claves:
        dic[clave] = [r.Population for r in registro if r.Country == claves]
    return dic


def grafica_poblacion_anyo_pais(registro, pais):
    dicc = population_country(registro, pais)
    X, Y = zip(*sorted(dicc.items()))
    titulo = 'Población por año desde 1995 hasta 2020'
    etiqueta_x = 'Año'
    etiqueta_y = 'Población'
    grafica(X, Y, titulo, etiqueta_x, etiqueta_y)
