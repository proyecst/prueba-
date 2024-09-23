import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import io

def lambda_handler(event, context):
    data = event['data']  # Datos de entrada de la función anterior
    df = pd.DataFrame(data)
    
    # Generar un buffer para Parquet
    buffer = io.BytesIO()
    pq.write_table(pa.Table.from_pandas(df), buffer)
    
    return buffer.getvalue()  # Devuelve el archivo Parquet
