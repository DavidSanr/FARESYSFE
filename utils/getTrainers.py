from os import listdir
from os.path import isdir, join, isfile, splitext
import pickle
import os
import face_recognition
from face_recognition import face_locations
from face_recognition.face_recognition_cli import image_files_in_folder
import re
import newTrainer

# region  Metodo para obtener los trainer en cada carpeta individual


def trainer_files_in_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(malpe)', f, flags=re.I)]

# endregion
# Metodo usado para añadir encode de las fotos a un array


def add_encode_to_array(cedulas):
    result = []
    encodeArray = []
    nameArray = []

    countPerson = 0
    countiterador = 0
    # *Variable con cada folder en la ubicacion dada
    for cedula in cedulas:
        countiterador = countiterador + 1
        print(countiterador)
        _trainer_patch = join('imagenes', cedula)
        try:
            folders = listdir(_trainer_patch)
            print(folders)
            # for class_dir in folders:

            # if not isdir(join(_trainer_patch, class_dir)):
            #     imagenes = image_files_in_folder(_trainer_patch)
            #     for imagen in imagenes:
            #         try:
            #             newTrainer.train_imagen(imagen)
            #         except Exception as Error:
            #             print(Error)

            countPerson = countPerson + 1
            print("Processing person", countPerson, "/", folders.__len__())
            #!Se crea una variable con el path completo de cada trainer
            trainers = trainer_files_in_folder(join(_trainer_patch, 'trainer'))
            countImage = 0
            for trainer_path in trainers:
                try:

                    countImage = countImage + 1
                    print("Procesando la imagen", countImage,
                          "/", trainers.__len__())
                    try:
                        with open(trainer_path, 'rb') as PickleFile:
                            encode = pickle.load(PickleFile)

                    except pickle.UnpicklingError as error:

                        print(error)
                    except Exception as error:
                        print(error)

                    encodeArray.append(encode[0])
                    nameArray.append(cedula)

                    continue

                except OSError:
                    print("Error al leer el archivo")
                    continue

                except:
                    print("Error desconocido")

        except OSError as error:
            print(error)
            pass
        except Exception as exception:
            print(exception)
            pass
    result = {"Name": nameArray, "Encoding": encodeArray}
    return result


# def readPerson(array_of_data):
#
#     result = []
#     for cedula in array_of_data:
#         print(cedula)
#         try:
#             add_encode_to_array(cedula[0:11])
#
#         except Exception as e:
#             print(e)
#             continue
# #
# #
# # readPerson()
