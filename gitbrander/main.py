from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
import json
import requests
import base64
import cv2 
# from docarray import Document

def inputTransformer(input_text=None):
    input_path = 'input'
    file_name = 'README.md'
    full_path = os.path.join(input_path, file_name)
    input_text = input_text or 'logo big green tree in circle'
    print(full_path, 'full_path')

    if not os.path.exists(input_path):
        os.makedirs(input_path)
        print('directory is created!', input_path)

    with open(full_path, 'w') as f:
        if os.path.getsize(full_path) == 0:
            f.write(input_text)

    readme = open(full_path,'r')
    readme_text = readme.read()
    readme.close()
    print(readme_text, 'readme_text')
    return readme_text


def outputTransformer(image=None):
    output_path = 'output/'
    image_name = 'logo.png'
    full_output_path = os.path.join(output_path, image_name)

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print("The new directory is created!", output_path)

    # Create new Image
    # if not image:
    #     img = Image.new(mode="RGB", size=(64, 64), color = (153, 153, 255))
    with open(full_output_path, 'wb') as f:
        f.write(image)

    # image.save("output/logo1.png", "PNG")
    im = Image.open(full_output_path).convert("L")

    
    # im = im.convert("1")
    # im = ImageEnhance.Color(im).enhance(0.0)
    # im = im.filter(ImageFilter.GaussianBlur(radius = .5))
    # im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV )
    # im.save("output/logo2.png", "PNG")

    # Convert to transparent
    # rgba = im.convert("RGBA")
    # im = im.convert("RGB")
        # im = ImageEnhance.Color(im).enhance(0.0)

    im = ImageEnhance.Brightness(im).enhance(1.2)
    im.save("output/logo3.png", "PNG")
    # im.save("output/logo4.png", "PNG")
    # im = ImageEnhance.Color(im).enhance(5.0)
    # im.save("output/logo5.png", "PNG")
    # im = ImageOps.posterize(im, 2)
    
    im = ImageOps.colorize(im, black ="blue", white ="white")

    im = ImageEnhance.Contrast(im).enhance(5.0)
    im.save("output/logo4.png", "PNG")
    im = ImageOps.autocontrast(im)
    im.save("output/logo5.png", "PNG")
    # datas = im.getdata()

    # Matrix = ( 1.1,   0,  0, 0, 
    #        0,   0.9,  0, 0, 
    #        0,     0,  1, 0) 

    # # Apply transform and save 
    # im = im.convert("RGB", Matrix)
    # im.save("output/logo8.png", "PNG")
    # newData = []
    # for item in datas:
    #     if item[0] <= 200 and item[1] <= 200 and item[2] <= 200:  # findingblack color by its RGB value
    #         # storing a transparent value when we find black color
    #         # newData.append((0, 128, 0, 0))

    #         newData.append((0, 128, 0))
    #     else:
    #         newData.append(item)  # other colours remain unchanged
    
    # im.putdata(newData)
    # im.save("output/logo9.png", "PNG")


def setData(prompt, num_images):
    return  {
        "text": prompt, 
        "num_images": num_images
    }

def setHeaders():
    return {
        "Bypass-Tunnel-Reminder": "go",
        "mode": "no-cors"
    }


# def fetchMega(prompt, num_images):
#     url = 'grpc://dalle-flow.jina.ai:51005'
#     da = Document(text=prompt).post(url, parameters={'num_images': num_images}).matches
#     da.plot_image_sprites(fig_size=(10,10), show_index=True)
#     payload = setData(prompt, num_images)
#     headers = setHeaders()
#     print(payload, 'payload')
#     response = requests.post(url, json=payload, headers=headers)
    
#     jsons = json.loads(response.text)
#     print(jsons)
#     return jsons

def fetchColab(prompt, num_images):
    url = 'https://chubby-groups-tell-35-189-160-197.loca.lt/dalle'
    payload = setData(prompt, num_images)
    headers = setHeaders()
    response = requests.post(url, json=payload, headers=headers)
    image_list = json.loads(response.text)
    return base64.b64decode(image_list[0])

if __name__ == "__main__":
    prompt = inputTransformer('Green alphabet letters A and B')
    image_one = fetchColab(prompt, 1)
    image = outputTransformer(image_one)