from os import listdir
from os.path import isdir, join, isfile, splitext
import pickle
import os



def createPath (first,*args):
    ruta = first
    for path in args:
        ruta = join(ruta,str(path))
    return ruta

def save_file(file,nombreArchivo:str,path:str,byteMode:bool) -> None: 

    method_lecture:str = 'wb'if byteMode else 'wt'
    try:
        if not isdir(path):
           os.makedirs(path)
        f = open(join(path,nombreArchivo),method_lecture)
        f.write(str(file)) if not byteMode else f.write(file)


    except OSError as e:
        print("Error al crear carpeta del archivo")

    except Exception as e: 
        print("Error desconocido")

def save_trainer(file,nombreArchivo:str,path:str) -> None: 

   
    try:
        if not isdir(path):
           os.makedirs(path)
        f = open(join(path,nombreArchivo),'wb')
        pickle.dump(file, f,pickle.HIGHEST_PROTOCOL)


    except OSError as e:
        print("Error al crear carpeta del archivo")

    except Exception as e: 
        print("Error desconocido")


def open_file(filename:str,path:str,byteMode:bool):
    method_lecture:str = 'rb'if byteMode else 'rt'
    filePath:str = join(path,filename)
    try:
        if not isdir(path):
            os.makedirs(path) 
        f = open(filePath,method_lecture)
        f.read()
        print("Archivo de person, exitosamente cargado")
        


    except OSError as e:
        print("Error al crear carpeta del archivo")
        print("No Existe") 

    except Exception as e: 
        print("Error desconocido")
        print("No Existe") 





    
    

    
