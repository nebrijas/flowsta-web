# Repositorio de trabajo del módulo de Periodismo de datos II
Herramientas digitales para la presentación y visualización de datos
## AADD
### AD1
Tal como os comentaba el jueves 9 de junio, la primera actividad consiste en comentar una pieza de periodismo de datos, visualización de datos o infografía con respecto a todo lo que sepáis previo a este máster o sobre los contenidos de este curso.

Es una excusa, entre otras, para practicar con Markdown. Es decir, hay que escribirlo en esta sintaxis.

No se exige un tamaño mínimo ni máximo pero si queréis orientación podéis hacerlo entre 300 y 500 palabras.

Habéis de practicar con:

- Encabezamientos
- Párrafos
- Listados
- Texto enfatizado en negrita y cursiva
- Enlaces
- Imágenes incrustadas

Hay muchos manuales, tutoriales. Os recomiendo el mío, que es sencillo: https://flowsta.github.io/markdown

Si no lo hicisteis el jueves, tenéis que crear un repositorio (proyecto) en **Github.com** a partir de https://github.com/nebrijas con el nombre compuesto por vuestra cuenta de Github, un guión corto medio y la palabra web. Es decir, en mi caso, dado que el usuario es "flowsta", la URL del nuevo proyecto sería:
```
https://github.com/nebrijas/flowsta-web
```

En este repositorio, al haberlo creado, habréis creado el archivo `README.md`. Podéis utilizarlo para escribir.

Recordad la particularidad de guardar los cambios de git que se denomina `commit` y lleva un mensaje de texto asociado. El martes 14 explicaremos más esto.

Podéis escribirme a aanton@nebrija.es si no estáis en el equipo del módulo, si tenéis cualquier duda o para cualquier otra cosa por "tonta" que os parezca. De estas cosas es de donde más aprendemos.

El martes 14 repasaremos los trabajos.

Un saludo
### AD2

Hola

#### Primera parte
Ahora que ya habéis hecho un documento `README.md` en Github vamos a hacer la segunda actividad. Y vamos a adelantar un poco para empezar a ver las posibilidades de Markdown, Github y la creación de una web.

Vamos a convertir nuestro repositorio en una web servida desde Github. Es decir, vamos a utilizar una funcionalidad de Github para funcionar no solo como servidor de git sino también como servidor WEB. Para ello hay que activar en la configuración de nuestro repositorio la opción *Pages* cuya URL es https://github.com/nebrijas/flowsta-web/settings/pages (cambiad flowsta por vuestra cuenta de github, si habéis seguido las instrucciones de la AD1 y habéis creado un repositorio con ese nombre). En *branch* (rama) elegimos `main` (no creo que tengáis otra) y en *folder* (directorio, carpeta) `root`.

Al activar esa opción y pasados unos segundos tendremos una web con un archivo `index.html` cuyo contenido es el contenido del `README.md` que se ha exportado/convertido a HTML en una URL parecida a esta (cambiad de nuevo flowsta por lo que corresponda):
```
https://nebrijas.github.io/flowsta-web
```

Hasta aquí lo podéis hacer ya si queréis. Luego, después de la próxima clase del jueves 16, podréis hacer lo siguiente.

#### Segunda parte
Para esta segunda parte tendremos que haber visto la herramienta (software) cliente de `git` para Windows (en Mac ya está instalado), [Git bash](https://gitforwindows.org/). Con ella:
- Clonaremos el repositorio remote, haremos una copia del repositorio remoto en local, es decir, en nuestro ordenador.
- Configuraremos git
- Realizaremos cambios en los archivos: crearemos un que llamaremos ad1.md a partir del archivo README.md
- Editaremos los archivos ad1.md y README.md para que su contenido corresponda con su nombre.
- En README.md tendremos que enlazar el archivo ad1.md
- Actualizaremos el repositorio remoto desde el local y comprobaremos que se han producido los cambios en remoto.
#### Tercera parte
Dado que si hacéis todo esto el archivo ad2.md parece que está vacío, esta actividad 2 tendrá una tercera parte que será comentar apropiadamente todo lo que se ha hecho como un ejercicio de programación literaria. Esto lo haremos después de la sesión del martes 21 de junio.
### AD3

Hola

Tal como empezamos a ver el martes 21 de junio, esta actividad dirigida 3 consiste en transformar uno de los ejercicios que se hicieron en programación, un código de Python para lograr un scraping de una web, en un ejercicio de programación literaria con Jupyter. De esta manera seguiremos trabajando con git, github y markdown pero también conoceremos Jupyter y veremos su potencia para aprovechar lo aprendido u olvidado de Python de cara a trabajar con datos.

He compartido por el pad el código pero [también podéis verlo en mi github](https://github.com/nebrijas/flowsta-web/blob/main/web-scraping.py).

Ese es el bruto que tendréis que transformar bajo el paradigma de la programación literaria, es decir, comentar mucho, lo más posible, para entenderlo no solo cuando lo estás haciendo sino cuando pase un tiempo hasta que lo vuelvas a ver, ese código de tal forma que el texto comentado es el hilo argumental del "cuaderno" que explica el código.

El archivo, tal como empezamos ayer, se llama ad3. En Jupyter esto significa que habrá creado un archivo "ad3.ipynb", donde "ipynb" viene de "interactive python notebook", cuanderno interactivo de python. Esta es la terminación de los archivos de los cuadernos de python.

Como habéis creado el archivo en la carpeta del repositorio tendréis un "ad3.ipynb" en la misma carpeta que "README.md" o "ad1.md". Lo tenéis que añadir a Github, es decir, primero a vuestro git local y luego subirlo al git remoto.

Mañana jueves veremos dudas sobre esto y también cómo guardar el archivo con otras extensiones para tener también un "ad3.md".

Recordad también que habiendo visto esto se puede hacer la tercera parte de la AD2.

Un saludo
### AD4
Hola

Para la AD4 hay que crear un cuaderno de Jupyter o "Jupyter Notebook" en la aplicación Jupyter.

Consiste en hacer un ejercicio de "programación literaria", es decir, contar de forma pormenorizada lo que hacemos con el código que ejecutamos. Lo contamos en celdas con Markdown y lo ejecutamos en celdas con Python.

En este cuaderno nos conectamos a la API covid19api.com y obtenemos los datos de España tal como nos cuenta la documentación de su API que se ha introducido en clase. Estos datos los incluimos en un "dataframe" o tabla de datos de Pandas, la librería de trabajo con datos tabulados de Python. Finalmente, se "plotean" los datos en forma de gráfico de línea.

Podemos lanzar Jupyter desde la propia carpeta del repositorio, para que los cambios se vayan guardando automáticamente, en el archivo ad4.ipynb

También tendremos que guardar una misma versión del archivo pero con terminación md, ad4.md

El pasado jueves 28 de junio realizamos una primera parte del ejercicio con los datos de España.

Hay que completar el trabajo con los datos de Centroamérica: Panamá, Costa Rica, Nicaragua, Guatemala, El Salvador y Honduras. Esto lo hemos visto en la clase del martes 5 de julio.

### Trabajo Final, TF
Hola

El trabajo final ya lo comenzamos a hacer con la AD1 por lo que quien tengas las aadd al día tendrá casi todo hecho. Es decir, este Trabajo Final consiste en tener una web pública con todos los trabajos que hemos hecho en este módulo.

Lo "único" que hay que hacer si has hecho lo demás es comprobar que desde README.md se puede acceder (con enlaces relativos) a todos los archivos de las aadd y que en este README se haga un ejercicio último de "programación literaria" sobre todo lo que se ha hecho en este módulo.
## Visualización
- [Visualización gráfica](https://es.wikipedia.org/wiki/Visualizaci%C3%B3n_(gr%C3%A1fica))
- [Minard](https://commons.wikimedia.org/wiki/File:Minard.png)
- [Visualización de datos](https://es.wikipedia.org/wiki/Visualizaci%C3%B3n_de_datos)
- [50 años de visualización de datos](https://es.wikipedia.org/wiki/Visualizaci%C3%B3n_de_datos#/media/Archivo:50_years_of_datavisulization_berengueres_own_work.png)
- 
## Herramientas
- [Repositorio del módulo](https://github.com/nebrijas/flowsta-web)
- [Pad colaborativo](https://semestriel.framapad.org/p/nebrijas-202122-online-9uvo?lang=es): identifíquense con su nombre y pongan un enlace en formato Markdown a un proyecto/artículo/publicación que les haya llamado la atención de periodismo y/o visualización de datos.

## Listado de actividades dirigidas:

- [Actividad dirigida 1](ad1.md)
- [Actividad dirigida 2](ad2.md)
- [Actividad dirigida 3](ad3.md)
- [Actividad dirigida 4](ad4.md)
- [Trabajo final](trabajo-final.md)

## Enlaces compartidos

Esto es un [pad](https://semestriel.framapad.org/p/nebrijas-202122-online-9uvo) para compartir algunos enlaces de trabajos interesantes de Periodismo y Visualización de Datos.
Poned vuestro nombre y proyecto en formato Markdown en este listado

- Adolfo: https://www.newtral.es/procesos-judiciales/20220516/
- Madelaine: Concentración y contratos sin competencia en compras para la salud mental en América Latina | Ojo Público (ojo-publico.com)
- Sergio Rivera. Herramienta digital creada por el diario La Nación de Argentina https://www.lanacion.com.ar/el-mundo/coronavirus-asi-es-avance-del-virus-se-nid2328201/
-Karol Lara. Son 34.361 y aumentan: Cómo la Lista cuenta el número de migrantes en Europa https://www.theguardian.com/world/2018/jun/20/the-list-europe-migrant-bodycount
- Marlene Testa  /https://www.nacion.com/data/divorcios-se-triplicaron-en-ultimas-tres-decadas/PV2BFG4CEJEN5G7QAMQS2VIBUE/story/
-Mixela Aparicio https://www.nacion.com/gnfactory/investigacion/2015/nacimientos/index.html
- Iria Santos: Todos ellos con visualizaciones muy variadas e interesantes desde el punto de vista periodístico al científico, pasando incluso por webdocs
 - https://www.linkedin.com/posts/ivo-van-breukelen-73204664_proptech-tech-innovative-activity-6944643803005800448-UGMS Se trata de una infografía animada con forma de donut, que muestra el avance a lo largo de los últimos 30 años del porcentaje de marcas de teléfonos móviles en el mercado según datos de manifactura de las propias compañías).
 - También considero muy interesantes los datos que se recogen en la página del Laboratorio de Datos de El Confidencial: https://lab.elconfidencial.com/
 - Datablog de The Guardian (https://www.theguardian.com/news/datablog+technology/data-visualisation)
 - los datos que recobe el CDV Lab de la Universidad de Coimbra (https://cdv.dei.uc.pt/)
 - el Laboratorio de RTVE (http://www.rtve.es/lab/). .
 - Por otro lado, yo sigo siendo fan del CDV Lab (Universidad de Coimbra), que es investigación, no periodismo, pero investigan sobre visualización de datos y tienen cosas muy chulas: https://cdv.dei.uc.pt
- Katia Allauca: Ola de calor y cambio climático https://elpais.com/opinion/2022-06-19/ola-de-calor-y-cambio-climatico.html
- Alejandro Reyes: Mapa del coronavirus en Estados Unidos del New York Times https://www.nytimes.com/es/interactive/2020/espanol/mundo/coronavirus-en-estados-unidos.html
- Zaida Herrera: Mapa: los resultados de las elecciones andaluzas por municipio. Medio RTVE https://www.rtve.es/noticias/20220619/andalucia-mapa-resultados-2022/2384299.shtml
- Fanny Arias: AMBA, la zona más crítica del país
https://www.lanacion.com.ar/sociedad/monitor-movilidad-asi-es-circulacion-ciudadanos-inicio-nid2426476/
-Tereza Espinoza: 
Aborto en Estados Unidos: el mapa que muestra dónde ya está prohibido y qué otros estados lo restringirán tras la sentencia de la Corte Suprema
 https://www.bbc.com/mundo/noticias-internacional-61806681
-Rubén Darío Sanjur: 
Casos de VIH y SIDA en España, en datos y gráficos. Datos actualizados el 9 de diciembre de 2021, presentados por el Ministerio de Sanidad, Servicios Sociales e Igualdad.
https://www.epdata.es/datos/casos-vih-sida-espana-datos-graficos/482/espana/106
-Karen García:  https://www.elespectador.com/colombia/mas-regiones/infografia-asi-vive-la-ninez-en-colombia-article/
-Cecilio Saldaña: Mapa sobre la votación de la resolución de la ONU contra la invasión Rusa a Ucrania https://elpais.com/internacional/2022-06-26/el-mundo-se-hunde-en-una-espiral-conflictiva-este-es-el-balance-de-fuerzas.html
- Graciela Cuevas: Reportaje visual en el que se explica, de forma didáctica, cómo se produce el contagio del coronavirus a través del aire y, sobre todo, en interiores. https://elpais.com/especiales/coronavirus-covid-19/un-salon-un-bar-y-una-clase-asi-contagia-el-coronavirus-en-el-aire/
-Alicia Valdés
https://lapromesarota.prodavinci.com/
 Este es un trabajo de periodismo de datos, referente a la investigación " La promesa rota: el colapso de la seguridad social en Venezuela". La presentación muestra con detalles el análisis de datos, con una visualización atractiva, colores que resaltan e infografías fáciles de entender.
- Jorge Barría Es un reportaje sobre cómo la izqueirda ha ido tomando ventaja en muchso países con el triunfo de Gustavo Petro y lo que se visualizaría en otros países de la región: Colombia gira a la izquierda con Petro: sus efectos en la región  https://www.connectas.org/analisis/gustavo-petro-colombia-izquierda/
- Einar Valdés. Utilizaré un reportaje que habla sobre el tráfico ilegal de las especies en peligro de extinción en España. https://www.elmundo.es/ciencia-y-salud/medio-ambiente/2021/12/30/61bcd569fc6c83a2308b459a.html
- Linda Batista: Mapa que detalla la madurez y el desempeño de los sistemas estadísticos de los países, considerando cinco áreas claves: https://www.worldbank.org/en/programs/statistical-performance-indicators
- Rigoberto Carranza: Estar en prisión provisional multiplica el riesgo de suicidio en la cárcel. Este trabajo es uno de los que seleccioné para realizar una de las Actividades Dirigidas. https://civio.es/2022/05/17/prision-provisional-suicidios-espana-covid-19/
- Maricarmen Camargo:  ¿Puede reducirse el fútbol a números? Cada vez hay más gente intentándolo https://elpais.com/politica/2021/06/17/actualidad/1623948023_002863.html
## Software
- [Bootstrap](https://getbootstrap.com/): plantillas para el desarrollo web.
- [Duckduckgo](https://duckduckgo.com/): buscador respetuoso con la privacidad de lxs usuarixs.
- [Etherpad](https://etherpad.org/): documentos de texto colaborativos en tiempo real
- [ffmpeg](https://ffmpeg.org/)
- [GIMP](https://gimp.org/), GNU Imagen Manipulation Program.
- [git](https://git-scm.com/): software de gestión de versiones.
- [Git for Windows](https://gitforwindows.org/)
- [GNU](http://www.gnu.org/), GNU Not Unix. Incluye la licencia GPL (General Public License).
- [ImageMagick](https://imagemagick.org/)
- [Inkscape](https://inkscape.org/), dibuja con libertad.
- [ObservableHQ](https://observablehq.com/), como los cuadernos de Jupyter pero con JavaScript.
- [Openshot](https://www.openshot.org/), editor de vídeo.
- [Pandas](https://pandas.pydata.org/): pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
- [Pandas Docs](https://pandas.pydata.org/pandas-docs/stable/pandas.pdf)
- [R](https://www.r-project.org/): The R Project for Statistical Computing
- [RStudio](https://www.rstudio.com/)
- [StackExchange](https://stackexchange.com/): el mejor sitio donde compartir y resolver problemas
- [SVG](https://www.w3.org/Graphics/SVG/): gráficos vectoriales para la web.
## Periodismo y Visualización de Datos
- [Journocoders](https://github.com/journocoders)
- [Max Harlow](https://github.com/maxharlow/tutorials)
## Redes sociales

### Telegram

- [Canal de Periodismo de Datos del Datalab](https://t.me/datosperiodismo)
- [Canal de Visualizar, grupo de visualización del Datalab](https://t.me/visualizar)
- [Canal de datos en general del Datalab](https://t.me/postDatalab)

### Slack

- [Periodismo Datos](https://join.slack.com/t/periodismodatos/), mantenido por Adolfo Antón Bravo. [Enlace de invitación válido hasta 2022-07-21](https://join.slack.com/t/periodismodatos/shared_invite/zt-1b9epysaa-u8r1cfmjaXBvEZI~l00Yvg). Cuenta con los siguientes canales:
 - academia
 - apps
 - convocatorias
 - covid19
 - data
 - educación
 - general
 - intros
 - lecturas
 - mpvd
 - random
 - salario

## Bibliografía
- [American Slavery As It Is](https://en.wikipedia.org/wiki/American_Slavery_As_It_Is)
- [El Lenguaje de los Nuevos Medios, de Lev Manovich](https://uea1arteycomunicacion.files.wordpress.com/2013/09/manovich-el-legunaje-de-los-nuevos-medios.pdf)
- [Gráfica](https://es.wikipedia.org/wiki/Gr%C3%A1fica)
- [Infografía](https://es.wikipedia.org/wiki/Infograf%C3%ADa)
- [Introducción al periodismo de datos](https://flowsta.github.io/periodismodatos/)
- [Manual básico de Markdown](https://flowsta.github.io/markdown)
- [Manual básico de git](https://flowsta.github.io/github)
- [Manual de git bash](https://www.geeksforgeeks.org/working-on-git-bash/)

## API Covid
- [Covid19 API](https://covid19api.com/)
- [API](https://api.covid19api.com/)
- [Documentación en Postman](https://documenter.getpostman.com/view/10808728/SzS8rjbc)
- 
- 
## Python
- [Requests](https://requests.readthedocs.io/en/latest/): HTTP for humans
- [Pandas](https://pandas.pydata.org/)
- [Tipos de gráficos](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html): pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.



### Librerías de visualización
- [Matplotlib](https://matplotlib.org/)
- [Bokeh](https://bokeh.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly](https://plotly.com/)

