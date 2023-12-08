import os
import subprocess

def convert_heic_to_jpg(source_directory, destination_directory, imagemagick_path):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for filename in os.listdir(source_directory):
        if filename.lower().endswith(".heic"):
            source_file = os.path.join(source_directory, filename)
            jpgname = os.path.splitext(filename)[0] + '.jpg'
            destination_file = os.path.join(destination_directory, jpgname)
            subprocess.run([os.path.join(imagemagick_path, "magick"), "convert", source_file, destination_file])
            print(f"Converted {filename} to JPG in {destination_directory}")

