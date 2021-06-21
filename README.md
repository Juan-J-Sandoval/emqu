# API
Esta API recibe un archivo `.xlsx`, que almacena en la ruta `dataFile/uploadedFile` despues valida que contenga una tabla con las siguientes columnas
* nombre
* apellido
* nacionalidad
* fechaContrato
* sexo  

Posteriormente limpia las filas de caracteres no funcionales y por último almacena la nueva tabla en un archivo `.csv` en la ruta `dataFile/validatedFile`.  
Las librerias que se utilizaron estan en el archivo `requirements.txt`. Para un buen funcionamiento es necesario generar un entorno virtual con el siguiente comando
```python
virtualenv nombre_de_tu_entorno -p python3
```
Posteriormente se activa con
```python
source nombre_de_tu_entorno/bin/activate
```
Ahora se instalan las librerias que vienen en el txt
```python
python -m pip install -r requirements.txt
```
Por último se inicia el archivo `run.py`
```python
python run.py
```
## Test
Para hacer pruebas a la API, se tiene que realizar una peticion metodo `POST`, con un body `multipart/form-data` y el archivo debe ir en una variable llamada `archivo`, de manera local la ruta seria `http://localhost:5000/uploads`.