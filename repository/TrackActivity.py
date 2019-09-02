
import pyodbc
from datetime import date,datetime





def load_status_process(connectionString, tabla) -> list:

    try:
        documents=[]
        # region Conexion a base de datos        conection = pyodbc.connect(connectionString)
        cursor = conection.cursor()
        # endregion
        # region query
        # cursor.execute('SELECT * FROM Personas as p where CONCAT(P.MunCie, P.SeqCie,P.VerCie) = \'40226199780\' ')
        query = f'SELECT [numero] FROM [trackActivity].[dbo].[{tabla}]  '
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

        # endregion


def match_number(number, fotoPath, fotoNombre):


    conection = pyodbc.connect(dbTrackActivitys)
    cursor = conection.cursor()
    query = f"INSERT INTO [trackActivity].[dbo].[FotoDescargas] ([id],[identificacion],[fecha],[estados]) VALUES(?,?,?)"
   
    cursor.execute(query, data)
    conection.commit()
    conection.close()
    cursor.close()


def insert_item_complete(connectionString, values):
    try:
        
        conection = pyodbc.connect(dbTrackActivitys)
        cursor = conection.cursor()
        query = f"INSERT INTO [trackActivity].[dbo].[foto_procesada] ([numero],[fecha]) VALUES(?,?)"
        cursor.execute(query, values)
        conection.commit()
    except pyodbc.Error as Error:
        print("Error de conexion")
        print(Error)
    except pyodbc.DatabaseError as Error:
        print("Error de base de datos")
        print(Error)
    except Exception:
        print("Error Desconocido")

# currenttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
# data = ('2222222222',currenttime,1)

# insert_item_complete(dbTrackActivitys, 'FotoDescargas', data)
