from flask import Flask, request
import os
import pandas as pd
app = Flask(__name__)

@app.route("/uploads", methods=['POST']) 
def uploads():
    response={}
    if request.method == 'POST':
        if "archivo" in request.files:
            fileNew = request.files['archivo']
            fileName = fileNew.filename
            fileNew.save(os.path.join('dataFile/uploadedFile', fileName))
            fileExcel=pd.read_excel(os.path.join('dataFile/uploadedFile/'+fileName))
            if set(['nombre','apellido','nacionalidad','fechaContrato','sexo']).issubset(fileExcel.columns):
                fileExcel.replace(to_replace=r'(\d)|(\')|(\-)', value='', regex=True,inplace=True)
                fileExcel.to_csv(os.path.join('dataFile/validatedFile/datos.csv'),index=True)
                response = {'code':200, 'body':{'FileName':'datos.csv','Message':'saved'}}
            else:
                response = {'code':400, 'body':{'Message':'El archivo no contiene las columnas necesarias'}}
        else:
            response = {'code':400, 'body':{'Message':'La variable "Archivo" no contiene archivo'}}
    return response

if __name__ == '__main__':
     app.run(port='5000', debug=True)