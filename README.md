# frogtek_prueba_tecnica

# Installation
- conda create --name django_env python=3.8
- conda activate django_env 
- pip install -r requirements.txt
- python main.py



- Install PostgreSQL locally. https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/. For mac:
   2.1. brew install postgresql
   2.2. brew services start postgresql
   2.3. Configure database server:
      2.3.1 Access postgress shell with: <strong><em>psql postgres</em></strong>
      2.3.2 Create Role: <strong><em>CREATE ROLE snowman WITH LOGIN PASSWORD 'snowball';</em></strong>
      2.3.3 Allow Role to create db: <strong><em>ALTER ROLE snowman CREATEDB;</em></strong>

El repositorio cuenta con 3 directorios:
- Data. Contiene un csv para desarrollar la parte 3 de Pandas/reporting (el csv generado
  está incluido en .gitignore para no subirse a github).
  
- Drafts. Notebooks empleados como borradores (sin estructurar)
  
- Respuestas. Contiene 3 notebooks:
    - Comprobaciones. Incluye algunas comprobaciones y análisis exploratorio de los
      datos de origen.
    - Parte1_SQL:
      1. Extracción de los csv de yellow taxis de Ene, Feb y Mar del año 2020 mediante
      web-scraping usando Requests y BeautifulSoup4.
      2. Con el contenido HTML obtenido se filtra por el año, mes(es) y tipo de taxi
         solicitados para obtener el link csv de los datos.
      3. La función csv_to_df(taxi_color, *month) lee los csv seleccionados,  realiza
         transformaciones de carácter FieldType (datetime, timedelta, incluir columna
         'mes', etc...) y devuelve un DataFrame de Pandas.
      4. Habiendo instalado PostgresSQL en local, se procede a crear una database de nombre
         'taxis' y una tabla de nombre 'yellowtaxis' usando el framework psycopg2.
      5. La función execute_batch() recoge el DataFrame previo y realiza un execute_batch
         a la DB creada previamente.
      6. Por último se incluyen las queries SQL que responden a las preguntas sobre los
         viajes más largos, cortos, medio y variaciones porcentuales de servicios de cada mes.
  
    - Parte3_reporting.
        1. Cargamos el csv tratado previamente en un DataFrame de Pandas (en el notebook
           de la Parte 1, justo debajo de la función csv_to_df() se encuentran unas líneas
           comentadas para la generación del csv en local, que se ignora al subir a github)
        2. Se realizan modificaciones a ciertos campos del dataframe para poder tratar los
           datos de manera que la tabla resultante cumpla con el formato solicitado en el
           enunciado.
        3. Se realiza una agrupación por 'mes', 'tipo_día' y 'RateCodeID' y suma del resto
           columnas para distribuir en 3 DataFrame los datos en función de su RateCodeID,
           que finalmente compondrán las 3 pestañas del excel solicitado.
  