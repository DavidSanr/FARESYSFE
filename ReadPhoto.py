from utils.trainer import encode_image
from utils.ActionWithFiles import createPath,save_file,open_file,save_trainer
import pyodbc
from LogService import save_log
from utils.variables import dbSic_ConnectionString,proxies,dbTrackActivitys,ftpFabioConfig,ftpFotoConfig,dbPasaportes
from repository.personaDb import load_persons 
from os import getcwd
from os.path import join
from utils.FetchTrainerForFTP import ftpDownload,ftp_upload
from face_recognition import load_image_file
from FaceRecognition import  encode_file_photo

from repository.PasaportesDB import  PasaportesDB
from repository.TrackActivity import load_status_process



def CreateTrainer():
    pasaporte = PasaportesDB(dbPasaportes)
    
    try:
        current_working_path = join(getcwd(),'resource')
        person_to_math =open_file('person_to_math.txt','resource',False)
        person_download = load_status_process(dbTrackActivitys,'FotoDescargas')
        
        
        if(person_to_math =='No Existe' or person_to_math == None):            
            person_to_math = load_persons(1)
            save_file(person_to_math,'person_to_math.txt','resource',False)
            print("Archivo de persona Localizado & cargado")
        persons = set(person_to_math) - set(person_download)
        for person in person_to_math:
            photo_path = join(current_working_path,person)
            ObjectFoto=pasaporte.getEntrada(person)
            if ObjectFoto is not None:
                save_file(ObjectFoto[14],f'{person}.jpeg',photo_path,True)       
                encode_face_person = encode_file_photo(join(photo_path,f'{person}.jpeg'))
                save_trainer(encode_face_person,f'{person}.malpe',join(current_working_path,person))
                save_log(person,'Face Complete','Logs')
                print("Proceso Completado")
        
 
    
    except IOError as error:
        currentPath = os.getcwd()
        print(error)
        save_log(cedula,error,'Logs')
        pass
    except Exception as error:
        print ("Error desconocido")
        save_log('no identificado',error,'Logs')
        pass
        

    


CreateTrainer()




