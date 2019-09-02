from DateTime.DateTime import datetime

class Foto:
    id:int
    ID_TipoIdentificacion:int
    Numero:str
    Foto_FhReferencia:datetime
    FotoRuta:str
    FotoNombre:str
    FuenteID:int
    FechaCreacion:datetime
    Activo:bool
    

    def __init__( self,id:int,ID_TipoIdentificacion:int,Numero:str,Foto_FhReferencia:datetime,FotoRuta:str,FotoNombre:str,FuenteID:int,FechaCreacion:datetime, Activo:bool):
        self.id = id
        self.Numero = Numero
        self.Foto_FhReferencia = Foto_FhReferencia
        self.FotoRuta = FotoRuta
        self.FotoNombre = FotoNombre
        self .FuenteID = FuenteID
        self.FechaCreacion = FechaCreacion
        self.Activo = Activo
