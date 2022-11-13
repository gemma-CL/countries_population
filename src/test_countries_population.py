from countries_population import *

def show_data(population):
    for p in population:
        print(p)

def test_calcula_paises(population):
    result = calula_paises(population)
    print(f'El número de países diferentes de los que se han recogido datos es: {result}')

def test_poblacion_pais_por_anyo(population, year, country):
    year = 2022
    country = 'Spain'
    result = poblacion_pais_por_anyo(population, year, country)
    print(f'Las poblaciones en {year} de {country} son: {result}')

def test_media_poblacion_pais(population, pais):
    pais = 'China'
    result = media_poblacion_pais(population, pais)
    print(f'La media de población de {pais} es: {result}')

def test_poblacion_mas_baja(population):
    resultado = poblacion_mas_baja(population)
    print(f'El país con la población más baja es: {resultado}' )

def test_agrupa_por_paises(population, pais):
    pais = 'China'
    result = agrupa_por_paises(population, pais)
    print(f'La poblacion de {pais} sido de: {result}')

def test_top_5_paises_mayor_poblacion(population):
    result = top_5_paises_mayor_poblacion(population)
    print(f'Los países en el top 5 son: {result}')

def main():
    population = lee_fichero('./data/countries_population.csv')
    show_data(population[:3])
    show_data(population[-3:])
    test_calcula_paises(population)
    test_poblacion_pais_por_anyo(population, 2022, 'Spain')
    ##test_media_poblacion_pais(population, 'China')
    ##test_poblacion_mas_baja(population)
    ##test_top_5_paises_mayor_poblacion(population)
    test_agrupa_por_paises(population, 'China')

if __name__ == "__main__":
    main()