from PIL import Image, ImageFilter
import os

image1 = Image.open('ninja.jpeg')
image1.rotate(90).save('ninja_rotated.jpeg')
image1.convert(mode='L').save('ninja_black_and_white.jpeg')
image1.filter(ImageFilter.GaussianBlur(5)).save('ninja_blurred.jpeg')

# image1.save('ninja.png')


'''
size_300 = (300, 300)

for f in os.listdir('.'):
    if f.endswith('.jpeg'):
        print(f)
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_300)
        # i.save(f'png_images/{fn}.png')
        i.save(f'300/{fn}_300{fext}')

'''
