
import pyodbc
from datetime import date

 from utils.variables import dbPasaportes,dbSic_ConnectionString,dbTrackActivitys








def calculate_yearsofbirth(age):
    _age = int(age)
    today = date.today()
    print(today)
    return today.year - _age


def load_persons(sexo:int,rango_edad = None) -> list:
#region NORMALIZAR 
    documents = []
    #Normaliza los valores obtenidos por paramentros, pasandolo a notacion de query
    _rango_edad_inicial = f'and year(FechaNacimiento) between \'{calculate_yearsofbirth(rango_edad[1])}\'' if rango_edad is not None else ''
    _rango_edad_secundaria = f'and \'{calculate_yearsofbirth(rango_edad[0])}\'' if rango_edad is not None else '' 
    _sexo = f'and Sexo = \'{sexo}\''
#endregion

    try:
        #region Conexion a base de datos
        conection = pyodbc.connect(dbSic_ConnectionString)
        cursor = conection.cursor()
        #endregion
        #region query 
        # cursor.execute('SELECT * FROM Personas as p where CONCAT(P.MunCie, P.SeqCie,P.VerCie) = \'\' ')
        query = f'SELECT [Cedula] FROM [dbSIC].[dbo].[vw_Personas] as p where cedula not like \'%000000000%\'{_sexo} {_rango_edad_inicial} {_rango_edad_secundaria} '
        print(query)
        cursor.execute(query) 
        rows = cursor.fetchall()
        
        for row in rows:
            documents.append(row[0])
        conection.close()
        return documents
    except pyodbc.Error as Error:
        print("Error de conexion")




        
        print(Error)
    except pyodbc.DatabaseError as Error:
        print("Error de base de datos")
        print(Error)
    except Exception:
        print("Error Desconocido")

        #endregion
def load_persons_with_photo():


    documents = []
    
    try:
        #region Conexion a base de datos
        conection = pyodbc.connect(connectionString)
        cursor = conection.cursor()
        #endregion
        #region query 
        # cursor.execute('SELECT * FROM Personas as p where CONCAT(P.MunCie, P.SeqCie,P.VerCie) = \'40226199780\' ')
        query = f'SELECT top(10) Numero FROM [Fotos].[dbo].[Fotos] where FuenteID in (9,13,15)'
        print(query)
        cursor.execute(query) 
        rows = cursor.fetchall()
        
        for row in rows:            
            documents.append(row[0])
        conection.close()
        return documents
    except pyodbc.Error as Error:
        print("Error de conexion")
    except pyodbc.DatabaseError as Error:
        print("Error de base de datos")
        print(Error)
    except Exception as e:
        print("Error Desconocido")
        print(e)


def load_person_status(cedula):
    conection = pyodbc.connect(dbSic_ConnectionString
                               )
    query = (f'SELECT TOP (10) [EstadoPersona] FROM [dbSIC].[dbo].[vw_Personas] where Cedula = \'{cedula}\' ')
    print(query)
    cursor = conection.cursor()
    cursor.execute(query)
    rows = cursor.fetchone()
    return rows[0]

def load_person_with_photo(cedula):
    result = []
    try:
        connection = pyodbc.connect(connectionString)
        query = f'SELECT numero,FotoRuta,FuenteID,FotoNombre FROM [Fotos].[dbo].[Fotos] where FuenteID in (9,15) and numero like ?'
        print(query)
        cursor = connection.cursor()
        cursor.execute(query,cedula)
        rows = cursor.fetchall()
        for row in rows:

            
            data = {'Numero':row[0],'FotoRuta':row[1],'FuenteID':row[2],'FotoNombre':row[3] }
            result.append(data)
        return result

    except pyodbc.Error as Error:
        print("Error de conexion")
        print(Error)
    except pyodbc.DatabaseError as Error:
        print("Error de base de datos")
        print(Error)
    except Exception as e:
        print("Error Desconocido")
        print(e)

    










