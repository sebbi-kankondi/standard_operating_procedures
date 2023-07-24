import os
from PIL import Image

def convert_images(input_dir, output_dir):
    # Check if output directory exists, if not create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get list of all .jpg files in the input directory
    jpg_files = [f for f in os.listdir(input_dir) if f.endswith('.jpg')]

    # Loop over all .jpg files
    for jpg_file in jpg_files:
        # Open the .jpg image file
        img = Image.open(os.path.join(input_dir, jpg_file))

        # Rotate the image 90 degrees to the right
        img = img.rotate(-90, expand=True)

        # Create the output file name by appending 2 at the end and keep them in jpg format
        new_file = os.path.splitext(jpg_file)[0] + '2' + '.jpg'


        # Save the image in .png format to the output directory
        img.save(os.path.join(output_dir, new_file))

# Use the function
convert_images('C:/Users/Sebbi Kankondi/Documents/National_Marine_Aquarium/aquarium_sop_book/images/generator',
                'C:/Users/Sebbi Kankondi/Documents/National_Marine_Aquarium/aquarium_sop_book/images/generator')
