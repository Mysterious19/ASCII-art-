from PIL import Image

CHAR_SET=[ ' ', '.', 'i', 'l', '@', '#']

if __name__=='__main__':
    
    image_filepath = '1.jpg'
    image = Image.open(image_filepath)
    
    #Scale image
    new_width=100
    (org_width,org_height)=image.size
    aspect_ratio = org_height/float(org_width)
    new_height = int(aspect_ratio*new_width)
    image = image.resize((new_width,new_height))
    
    #converting image to grayscale
    image=image.convert('L')

    #map charset to pixels
    range_width=50
    pixels_data = list(image.getdata())
    pixels_to_chars = [CHAR_SET[int(pixel/range_width)] for pixel in pixels_data]

    pixels_to_chars="".join(pixels_to_chars)

    new_image = [pixels_to_chars[i:i+new_width] for i in range(0,len(pixels_to_chars),new_width)]

    new_image= "\n".join(new_image)
    print(new_image)

