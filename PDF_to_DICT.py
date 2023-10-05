import camelot
import pandas as pd
import os

def pdf_to_dict(pdf_path, decryptkey, keys):

    tables = camelot.read_pdf(pdf_path,flavor='stream', pages='all', password=decryptkey)

    dfs = []
    i = 1

    while i < len(tables):
        df = tables[i].df
        i+=1
        dfs.append(df)

    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.columns = keys
    dictdata = combined_df.to_dict("records")
    
    return dictdata

## Nombres de las columnas de la tabla
keys = ["Movimiento","Fecha operacion", "Fecha Valor", "Concepto", "Cargos", "Abonos", "Saldo"]

## Direccion al archivo pdf
filename = "8 agosto BBVA mundial.pdf"
pdf_path = os.path.abspath(filename)

## Contraseña del archivo
decrypt = "811037781"

## Lista de diccionarios extraida del PDF
data = pdf_to_dict(pdf_path, decrypt, keys) 
print(data)
