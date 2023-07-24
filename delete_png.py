import os
import glob

# Define the directory
dir_path = "C:/Users/Sebbi Kankondi/Documents/National_Marine_Aquarium/aquarium_sop_book/images/display"

# Create a list of all png files and files ending with '2' in their names
files_to_delete = glob.glob(os.path.join(dir_path, "*.png")) + glob.glob(os.path.join(dir_path, "*2.*"))

# Iterate over the list and delete each file
for file_path in files_to_delete:
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting file: {file_path}. {e}")
