import os
import json

proxies = {
    "http": os.environ.get('PROXY_HTTP'),
    "https": os.environ.get('PROXY_HTTPS'),
}


#!Definir las creedenciales y el host del servidor FTP a conectar
ftpConfig =  {
"host": os.environ.get('FTPCONFIG_HOST'),
"port": 21,
"user": os.environ.get('FTPCONFIG_USER'),
"password": os.environ.get('FTPCONFIG_PASS')

}

ftpFaceRecoConfig = {
"host": os.environ.get('FTPCONFIG_FACE_HOST'),
"port": 21,
"user": os.environ.get('FTPCONFIG_FACE_USER'),
"password": os.environ.get('FTPCONFIG_FACE_PASSWORD')
}

ftpFotoConfig =  {
"host": os.environ.get('FTP_FOTO_HOST'),
"port": 21,
"user": os.environ.get('FTP_FOTO_HOST'),
"password": os.environ.get('FTP_PASS_HOST')
}

dbSic_ConnectionString:str = os.environ.get('DBSIC_CONNECTIONSTRING')
dbTrackActivitys:str = os.environ.get('DBTRACKACTIVITY_CONNECTIONSTRING')
dbPasaportes:str = os.environ.get('DBPASAPORTE_CONNECTIONSTRING')



def getFuenteFolder(fuenteID):
    operators:dict = {
            1: '',
            8: 'JUSTICIA-II',
            9: 'Licencia',
            11: 'Justicia-II',
            12:'Prisiones',
            13: 'Pasaporte',
            14:'DGM',
            15: 'MIP',
            16:'Biometrico'



                    }
    result = operators.get(fuenteID, lambda :'operacion no validad')
    return result


# def readFromEnviroment(variable):
#     var = os.environ.get('SICDB')
#     var = json.loads(var)
#     print(var)

# readFromEnviroment("SicDB")

