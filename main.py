from unittest import result
from PIL import Image
import cv2
import os

def resize_img( imge):
    img_resize = Image.open("img2/"+imge)
    new_img = img_resize.resize((1180,960))
    return new_img
    

#example
def main():
    print("resize image!")
    image = Image.open('bg_main.jpg')
    #image.show()
    print(image.format) # Output: JPEG

    print(image.mode) # Output: RGB

    print(image.size) # Output: (1920, 1280)

    print(image.palette) # Output: None
    image_bg = Image.open('big.jpg')
    new_image = image_bg.resize((1180,960))
    new_image.save('img_fix_size.jpg')
    print("fix size",new_image.size)
    #new_image.show()
    print("width", new_image.width, new_image.height)

    # past image resize 
    logo = Image.open('img_fix_size.jpg')
    image_bg = image.copy()
    position = ( 50, 50)
    #position = ((image_bg.width - logo.width), (image_bg.height - logo.height))
    print("position",position)
    image_bg.paste(logo, position)
    image_bg.save('pasted_image.jpg')
    #image_bg.show()

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        #process resize img
        if filename is not None:
           resize_name = resize_img(filename)
           resize_name.save("result/"+ filename)
           #resize_name.show()
           #print("filname",filename)
        
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

#process past image
def load_image_result(folder):
    image_main = Image.open('bg1.jpg')
    position = ( 50, 50)

    for filename in os.listdir(folder):
        print("file name", filename)
        logo = Image.open("result/"+filename)
        image_bg = image_main.copy()
        image_bg.paste(logo, position)
        image_bg.save("out/"+filename)
        #image_bg.show()

if __name__ == "__main__":
    main()
    images = load_images_from_folder("img2")
    load_image_result("result")
    #print("images", images)
    #for filename in os('img2'):
	    # load image
	    #img_data = Image.imread('img2/' + filename)
	    #store loaded image
	    #loaded_images.append(img_data)
	    #print('> loaded %s %s' % (filename, img_data.shape))
