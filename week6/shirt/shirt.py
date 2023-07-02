# The program expects exactly two command-line arguments, then overlay shirt.png
# (which has a transparent background) on the input after resizing and cropping
# the input to be the same size, saving the result as its output.
# The program exits via sys.exit:
# -if the user does not specify exactly two command-line arguments,
# -if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
# -if the input’s name does not have the same extension as the output’s name, or
# -if the specified input does not exist.

import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_argv()

    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')

    shirt_file = Image.open('shirt.png')

    size = shirt_file.size

    muppet = ImageOps.fit(image_file, size)
    muppet.paste(shirt_file, shirt_file)
    muppet.save(sys.argv[2])


def check_command_line_argv():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if check_extension(file1[1]) == False:
        sys.exit('Invalid input')
    elif check_extension(file2[1]) == False:
        sys.exit('Invalid output')
    elif file1[1].lower() != file2[1].lower():
        sys.exit('Input and output have different extensions')

def check_extension(file):
    return file in ['.jpg', '.jepg', '.png']

if __name__ == '__main__' :
    main()