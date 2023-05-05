from dotenv import load_dotenv # load_dotenv lee .env
import os

load_dotenv() #Esto permite la carga de los elementos de .env como variables de entorno

user = os.environ["USER"]
password = os.environ["PASSWORD"]
host = os.environ["HOST"]
database = os.environ["DATABASE"]
server = os.environ["SERVER"]

DATABASE_CONNECTION_URI = f'{server}://{user}:{password}@{host}/{database}' #Esta linea va a contruir la conexion para podernos conectar a la base de datos
print(DATABASE_CONNECTION_URI)
