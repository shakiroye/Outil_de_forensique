import exifread

def get_exif(file_name):
    with open(file_name, "rb") as file:
        exif = exifread.process_file(file)
    if not exif:
        print("Aucune métadonnée EXIF.")
    else:
        for tag in exif.keys():
            print(tag + " " + str(exif[tag]))

get_exif('resources/photo.jpg')