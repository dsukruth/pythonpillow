from PIL import Image,ImageFilter //importing python pillow library

im=Image.open("dhanush1.jpg") //image you want to rotate
rotate_angle= 90              //rotate angle is 90 degree
im.rotate(rotate_angle).save("dhanush2.jpg")// to save the rotated rotate_angle
