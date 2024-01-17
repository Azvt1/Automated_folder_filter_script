import os
import shutil
from datetime import datetime

def organise_files(source_folder, destination_folder):

    # Check if source folder really exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does NOT exists ")
        return
    else:
        print("exists")
    for filename in os.listdir(source_folder): 
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            file_type = filename.split(".")[-1].lower()
            type_folder = os.path.join(destination_folder, file_type)
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)
            unique_filename = filename
            count = 1
            while os.path.exists(os.path.join(type_folder, unique_filename)):
                base_name, extension = os.path.splitext(filename)
                unique_filename = f"{base_name}_{count}{extension}"
                count += 1

            destination_path = os.path.join(type_folder, unique_filename)
            shutil.move(file_path, destination_path)

            print(f"Moved: {filename} -> {destination_path}")




source_folder = "Specify your source folder"
destination_folder = "Specify your destination folder"
organise_files(source_folder, destination_folder)
    