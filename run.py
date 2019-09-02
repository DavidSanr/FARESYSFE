from utils.variables import ftpFabioConfig,ftpFaceRecoConfig,ftpFotoConfig,dbTrackActivitys,dbPasaportes,getFuenteFolder
from LogService import save_log_error,save_log
from repository.PasaportesDB import PasaportesDB
from repository.personaDb import load_persons_with_photo,load_persons,load_person_with_photo
from repository.TrackActivity import load_status_process,insert_item_complete
from utils.trainer import encode_image
from utils.FetchTrainerForFTP import ftpDownload
from utils.ActionWithFiles import save_file,save_trainer
from datetime import datetime
from os.path import join
from ftplib import all_errors as FTPERROR


def create_trainer_model():
    PasaporteRepository = PasaportesDB(dbPasaportes)
    try:
        persons_to_encode = load_persons_with_photo()
        persons_ready_encode = load_status_process(dbTrackActivitys,'foto_procesada') or ''
        persons_to_encode_from_pasaporte = PasaporteRepository.get_all_data()
        persons_to_process = set(persons_to_encode) - set(persons_ready_encode) 
        persons_to_process =  set(persons_to_encode_from_pasaporte) - set(persons_to_process) 
        for person in persons_to_process:
            date =datetime.now()
            person_information = load_person_with_photo(person)
            
            person_photo_from_pasaporte  =PasaporteRepository.getEntrada(person)
            count = 0 
            if person_photo_from_pasaporte != None :
                rutaGuardado = join('resource',person)
                save_file(person_photo_from_pasaporte[1],f'{person}-13.jpeg',rutaGuardado,byteMode=True)
                
            for pi in person_information:
                
                count = count + 1
                filename = pi.get('FotoNombre')
                fuenteId = pi.get('FuenteID')
                FotoRuta = pi.get('FotoRuta')
                print(fuenteId)
                try:
                    ftpDownload(person,ftpFotoConfig,getFuenteFolder(fuenteId),filename,FotoRuta)
                except FTPERROR as e:
                    print(e)
                    continue
            insert_item_complete(dbTrackActivitys,[person,date])
            
            
            


    except Exception as E:
        print(E)
        save_log_error(E,'log',person)
        

       





create_trainer_model()













