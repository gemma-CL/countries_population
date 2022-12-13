from countries_population import *


def show_data(population):
    for p in population:
        print(p)

def test_calcula_paises(population):
    result = calula_paises(population)
    print(f'El número de países diferentes de los que se han recogido datos es: {result}')

def test_poblacion_pais_por_anyo(population, year, country):
    result = poblacion_pais_por_anyo(population, year, country)
    print(f'La población en {year} de {country} es: {result}')

def test_media_poblacion_pais(population, pais):
    result = media_poblacion_pais(population, pais)
    print(f'La media de población de {pais} es: {result}')

def test_poblacion_mas_baja(population):
    resultado = poblacion_mas_baja(population)
    print(f'El país con la población más baja es: {resultado}' )

def test_agrupa_por_paises(population, pais):
    result = agrupa_por_paises(population, pais)
    print(f'La poblacion de {pais} ha sido de: {result}')

def test_top_5_paises_mayor_poblacion(population):
    result = top_5_paises_mayor_poblacion(population)
    print(f'Los países en el top 5 son: {result}')

def test_total_migrantes_pais(population, pais):
    result = total_migrantes_pais(population, pais)
    print(f'El total de migrantes que ha tenido {pais} es: {result}')

def test_total_migrantes_paisD(population, pais):
    result = total_migrantes_paisD(population, pais)
    print(f'El total de migrantes de {pais} en los últimos años ha sido: {result}')

def test_pais_menor_fertilidad_anyo(population, year):
    result = pais_menor_fertilidad_anyo(population, year)
    print(f'El país con menor fertilidad en {year} es: {result}')

def test_mayor_porcentaje_pop_urbana(population, pais):
    result = mayor_porcentaje_pop_urbana(population, pais)
    print(f'El mayor procentaje de población urbana que ha tenido {pais} es: {result}')

def test_top_7_paises_densidad_km2_anyo(population, year):
    result = top_7_paises_densidad_km2_anyo(population, year)
    print(f'Los 7 países con más densidad por kilómetro cuadrado en {year} son: {result}')

#TEST BLOQUE 4
def test_grafica_poblacion_anyo_pais(population, pais):
    result = grafica_poblacion_anyo_pais(population, pais)
    print(result)


def main():
    population = lee_fichero('./data/countries_population.csv')
    show_data(population[:3])
    show_data(population[-3:])
    #test_calcula_paises(population)
    #test_poblacion_pais_por_anyo(population, 2020, 'Spain')
    #test_media_poblacion_pais(population, 'China')
    #test_poblacion_mas_baja(population)
    #test_top_5_paises_mayor_poblacion(population)
    #test_agrupa_por_paises(population, 'China')
    ##test_total_migrantes_pais(population, 'China')
    ##test_total_migrantes_paisD(population, 'China')
    #test_pais_menor_fertilidad_anyo(population, 1995)
    #test_mayor_porcentaje_pop_urbana(population, 'Spain')
    test_grafica_poblacion_anyo_pais(population, 'Norway')
    #test_top_7_paises_densidad_km2_anyo(population, 2000)
if __name__ == "__main__":
    main()