from PIL import Image, ImageDraw, ImageFilter

image1 = Image.open('aston-martin.jpg')
image2 = Image.open('lorem-face.jpg')

resize_image1 = image2.resize((500, 500))

image1.paste(resize_image1, (650, 650))

converted_image1 = image1.convert('RGB')
converted_image1.show()
converted_image1.save('pasted-image.jpg', quality=95)