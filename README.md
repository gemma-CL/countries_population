# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  2022/23)
Autor/a: Gemma Catalano Llamas   uvus:GMQ0523

Este proyecto recoge los datos de la población de diferentes países del mundo. El dataset no contaba con una columna del tipo fecha, por lo que se ha añadido un columna más, siendo 15 las columnas totales.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<population.py\>**: Aquí encontramos las funciones principales.
  * **\<population_test.py\>**: En este módula testeamos las funciones del módulo population.py.
* **/data**: Contiene el dataset del proyecto.
    * **\<countries_population.csv\>**: Contiene los datos con los que vamos a trabajar relacionados con la población de diferentes países.
    
## Estructura del *dataset*

El dataset está compuesto por \<17\> columnas, con la siguiente descripción:

Month, Year, Country, Population, Yearly_percentage_Change, Yearly_Change, Migrants_net, Median_Age, Fertility_Rate, Density_PKm2, Urban_Pop_percentage, Urban_Population, Countrys_Share_of_World_Pop_percentage, World_Population, Country_Global_Rank, War, Partner

* **\<Month>**: de tipo \<int\>, representa el mes en el que los datos se tomaron.
* **\<Year>**: de tipo \<int\>,, representa el año en el que se tomaron los datos.
* **\<Country>**: de tipo \<str\>, representa el nombre del país.
* **\<Population>**: de tipo \<int\>, representa la población total de dicho país.
* **\<Yearly_percentage_Change>**: de tipo \<str\>, representa el porcentaje del cambio en el censo del país.
* **\<Yearly_Change>**: de tipo \<int\>, representa la cantidad en exacta en la que fluctua la población.
* **\<Migrants_net>**: de tipo \<int\>, representa la cantidad de migrantes que tuvo el país.
* **\<Median_Age>**: de tipo \<str\>, representa la edad media con la que se tiene hijos en el país.
* **\<Fertility_Rate>**: de tipo \<str\>, representa el índice de fertilidad del país.
* **\<Density_Pkm2>**: de tipo \<float\>, representa el número de personas que hay por kilómetro cuadrado en el país.
* **\<Urban_Pop_percentage>**: de tipo \<str\>, representa el porcantage de población urbana en el país.
* **\<Urban_Population>**: de tipo \<str\>, representa el número de población urbana del país.
* **\<Countrys_Share_of_World_Pop_percentage>**: de tipo \<str\>, representa el porcentaje que representa el país de la población total mundial.
* **\<World_Population>**: de tipo \<str\>, representa la poblacíon mundial.
* **\<Country_Global_Rank>**: de tipo \<int\>, representa el ranking mundial del país.
* **\<War>**: de tipo \<bool\> representa que el país wn cuestion estuvo en guerra.
* **\<Partner>**: de tipo \<str\> representa el aliado del país.
* **\<exact_date>**: de tipo \<datetime\>, representa una fecha exacta.
....

## Tipos implementados

Aquí se encuentra una namedtuple llamada Countries_Population.
Countries_Population = namedtuple('Countries_Population', 'Month, Year, Country, Population, Yearly_percentage_Change, Yearly_Change, Migrants_net, Median_Age, Fertility_Rate, Density_PKm2, Urban_Pop_percentage, Urban_Population, Countrys_Share_of_World_Pop_percentage, World_Population, Country_Global_Rank, War, Partner, exact_date')


## Funciones implementadas

En este proyecto se encuentran las siguientes funciones.


### \<countries_population.py\>

* **<lee_fichero(fichero)>**:lee los datos del fichero csv y devuelve una lista de tuplas de tipo Info con los datos del fichero.
* **<parsea_bool(war)>**: devuelve True si el país estuvo en guerra.
* **<calcula_paises(registros)>**: calcula el número total de países diferentes de los que se han recogido datos.
* **<poblacion_pais_por_anyo(registro, years, pais)>**: muestra la poblacion de un país en un año determinado.
* **<media_poblacion_pais(registro, pais)>**: muestra la media de la población de dicho país.
* **<poblacion_mas_baja(registro)>**: muestra el país que ha tenido la población más baja.
* **<top_5_paises_mayor_poblacion(registro)>**: nos muestra los países del top 5 mundial.
* **<agrupa_por_paises(registro)>**: devuelve las poblaciones que ha tenido dicho país.
* ...

### \<test_countries_population.py\>

En el módulo de pruebas se han definido las siguientes funciones de pruebas, cada una de las cuales se usa para probar la función en el módulo countries_population.py.
* ...
* 

