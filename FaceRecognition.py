from flask import jsonify
import pickle
import re
import face_recognition
import numpy
import os
from face_recognition import face_locations,face_locations,face_encodings




def reco_face(file,data):
    name = ''
    distancefoto = []    

    while True:
        imagen = face_recognition.load_image_file(file)

        try:
            face_locations = face_recognition.face_locations(imagen, number_of_times_to_upsample=1, model="hog")
            if len(face_locations) < 1:
                return jsonify({"message": "No se encontro ningun rostro en la imagen"})
                # face_locations = face_recognition.face_locations(rotate(imagen,1.57))

            face_encodings =  face_recognition.face_encodings(imagen, face_locations)


        except IndexError:
            return jsonify("Error al cargar la codificacion de la fotografia, prueba otra.")

        calc = {"Nombre": "No encontrado", "Distancia": "indefinido"}
        data_encoding = data["Encoding"]

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            matches = face_recognition.compare_faces(data_encoding, face_encoding, tolerance=0.455)
    
            if True in matches:
                first_match_index = matches.index(True)
                name = data["Name"][first_match_index]
                distancefoto = face_recognition.face_distance(data_encoding, face_encoding).tolist()
                calc = {}
                if (len(calc) < 0):
                    calc = ({'Nombre': "No encontrado ", 'Distancia': 'indefinido'})
                calc = ({'Nombre': name, 'Distancia': distancefoto[first_match_index]})

        return jsonify({"Identificador": calc['Nombre']})



def encode_file_photo(path):
    
    try:
        imagen = face_recognition.load_image_file(path)
        face_locations = face_recognition.face_locations(imagen, number_of_times_to_upsample=1, model="hog")
        if len(face_locations) < 1:
            return jsonify({"message": "No se encontro ningun rostro en la imagen"})
                # face_locations = face_recognition.face_locations(rotate(imagen,1.57))

        face_encodings =  face_recognition.face_encodings(imagen, face_locations)
        return face_encodings


    except IndexError:
        return jsonify("Error al cargar la codificacion de la fotografia, prueba otra.")