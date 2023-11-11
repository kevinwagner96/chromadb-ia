import time
import pandas as pd
from googletrans import Translator

translator = Translator()
INDEX = 0


def traducir_a_espanol(texto):
    global INDEX
    INDEX = INDEX + 1
    progres = INDEX/10
    if progres % 20 == 0:
        time.sleep(60)

    print('\rTraduciendo al español [%d%%]'%progres, end="")
    traduccion = translator.translate(texto, dest='es')
    return traduccion.text


archivo_origen = 'imdb_top_1000.csv'
archivo_destino = 'imdb_top_1000_es.csv'
columna_a_traducir = 'Overview'
columnas_a_mover = ['Overview', 'Series_Title', 'Released_Year']

df_origen = pd.read_csv(archivo_origen)
df_origen[columna_a_traducir] = df_origen[columna_a_traducir].apply(traducir_a_espanol)
nuevo_df = df_origen[columnas_a_mover]
nuevo_df.to_csv(archivo_destino, index=False)
