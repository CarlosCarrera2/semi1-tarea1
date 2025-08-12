 ### Crear entorno virtual
 ```bash
 python -m venv .venv

# Activarlo en windows
 .venv\Scripts\activate

 # Activarlo en linux
 source .venv/bin/activate
 ```

 ### Instalar Flask y CORS
 ```bash
 pip install Flask

 # Si es necesario se puede instalar cors
 pip install flask-cors
 ```

 ### Generar el archivo con las dependencias
 ```bash
 pip freeze > requirements.txt
 ```

 ### Instalar las dependencias
 ```bash
 pip install -r requirements.txt
 ```
 