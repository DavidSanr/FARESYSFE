from face_recognition import face_distance,face_locations


# Sacar la distancia euclediana del rostro de la foto!


def encode_image(image_path):
    encode = []
    image = face_recognition.load_image_file(image_path)
    faces_bboxes = face_locations(image)
    if len(faces_bboxes) != 1:
        return "No hay caras en esta imagenes "
    encode.append(face_recognition.face_encodings(
        image, known_face_locations=faces_bboxes)[0])

    return encode
