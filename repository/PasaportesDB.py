from utils.variables import dbPasaportes,dbSic_ConnectionString,dbTrackActivitys
import pyodbc
from LogService import save_log_error

class PasaportesDB():

    def __init__(self,ConnectionString):
        self.ConnectionString = ConnectionString


    def connectDB(self):
        connection = pyodbc.connect(self.ConnectionString)        
        return connection
    

    #Region GET ALL CEDULA

    #Busca todas las cedulas correspondientes a los registros de pasaportes

    #--------------------------------------------------------------------------------------------------------------------------------------------------

    def get_all_data(self):
        data = []
        connection = self.connectDB()
        cursor:pyodbc.Cursor = connection.cursor()
        # query:str = 'select [Cedula] from PasaportesPro' 
        query:str = '''
        SELECT Cedula
        FROM [Pasaportes].[dbo].[PasaportesPro]
        where Cedula is not null  and Cedula != ''
        group by Cedula
        HAVING 
        LEFT(Cedula,3)>='001' AND 
        LEFT(Cedula,3)<='402' AND
        LEN(CEDULA) IN (11,13)

        '''
        try:
            rows = cursor.execute(query).fetchall()
            for row in rows:
                data.append(row[0])

            
            return data
        
        except pyodbc.OperationalError as e:
            print('Error en la base de datos')
            save_log_error(cedula,e,'log')
        except TypeError as e :
            print('ERROR EN LA CONVERSION')
            print(e)
            save_log_error(cedula,e,'log')

        except Exception as e:
            print("error desconocido")
            print(e)
            save_log_error(cedula,e,'log')
    #--------------------------------------------------------------------------------------------------------------------------------------------------
   
    #EnRegion

    #Region Busqueda por Identificacion
    #Busca la coincidencia con el registro unico de cedula
    def getEntrada(self,Cedula):        
        connection = self.connectDB()
        cursor:pyodbc.Cursor = connection.cursor()       
        query:str = "SELECT Cedula,DocumentImage FROM PasaportesPro where Cedula like ? order by FechaPasaporte desc "  
        try:  
            rows = cursor.execute(query,Cedula).fetchone()      
            data= list(rows)# or simply data.append(list(row))
            return data

        except pyodbc.OperationalError as e:
            print('Error en la base de datos')

        except TypeError as e :
            print('ERROR EN LA CONVERSION')

        except Exception as e:
            print("error desconocido")
            print(e)

    #EndRegion 
#--------------------------------------------------------------------------------------------------------------------------------------------------
   
    
        



    
        
        
        

