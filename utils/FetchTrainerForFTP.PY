import os
from os.path import join
from ftplib import FTP,all_errors as ftperrors
from utils.variables import ftpFabioConfig,ftpFotoConfig
from LogService import save_log_error
global contar
global urlList




#Region
#Metodo para descargar Fotos del FTP
#----------------------------------------------------------------------------------------------------------------------------------------------------#
def ftpDownload(cedula,ftpConfig,fuente,fotoNombre,fotoRuta):
    host = ftpConfig["host"]
    port = ftpConfig["port"]
    user = ftpConfig["user"]
    password = ftpConfig["password"]
    path = fotoRuta
    filename =  fotoNombre
    rutaGuardado = join('resource',cedula)
    ftp = FTP()
    try:
        ftp.connect(host,port)
        ftp.login(user, password)
        ftp.cwd(path)
        if not os.path.exists(rutaGuardado):
            os.makedirs(rutaGuardado)
    
        ftp.retrbinary("RETR " + filename, open(join(rutaGuardado,filename), 'wb').write)
   
        ftp.quit()
        rutaFile = join(rutaGuardado,filename) 
        return print("Proccess be done!",rutaFile)
    except ftperrors as e:
        error_code = str(e).split(None,1)[0]
        save_log_error(cedula,error_code,'log')

#----------------------------------------------------------------------------------------------------------------------------------------------------#
#EndRegion

#Region Metodo para SUBIR DATOS FTP 
#----------------------------------------------------------------------------------------------------------------------------------------------------#
# def ftp_upload(cedula:str,ftpconfig:list,path:str,data) -> None:
#     ftp:FTP() = FTP()
#     host = ftpConfig["host"]
#     port = ftpConfig["port"]
#     user = ftpConfig["user"]
#     password = ftpConfig["password"]
#     filename = f'{cedula}.malpe'
#     try:
#         ftp.connect(host,port)
#         ftp.login(user,password)
#         ftp.cwd('home')
        
#             directories  = ftp.dir()
#             if path in directories:
                
#                 ftp.cwd(path)
#             else:
#                 ftp.makedirs(path)
#             all_files = ftp.dir()   
#             if cedula in all_files 
#             else ftp.makedirs(cedula)
#             ftp.cwd(cedula)
#             ftp.storbinary('STOR %s' % filename, data) 
#         except ftperrors :

#             error_code = str(e).split(None,1)[0]
#             save_log_error(cedula,error_code,'log')
#     except ftperrors as e:
        
#         save_log_error(cedula,error_code,'log')                   
#----------------------------------------------------------------------------------------------------------------------------------------------------#
#EndRegion               


    


                






         
            
            




#EndRegion




