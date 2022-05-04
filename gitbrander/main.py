from PIL import Image, ImageEnhance
import os
import json
import requests
import base64
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
    img1 = Image.open(full_output_path)
    # im3 = ImageEnhance.Color(im)
    img2 = ImageEnhance.Contrast(img1).enhance(0.0)
    img3 = ImageEnhance.Brightness(img2).enhance(2.0)
    

    # Convert to transparent
    rgba = img.convert("RGBA")
    datas = rgba.getdata()
    
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:  # finding white color by its RGB value
            # storing a transparent value when we find a white color
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)  # other colours remain unchanged
    
    rgba.putdata(newData)
    rgba.save("output/logo2.png", "PNG")


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
    url = 'https://cold-clocks-wave-35-229-140-35.loca.lt/dalle'
    payload = setData(prompt, num_images)
    headers = setHeaders()
    response = requests.post(url, json=payload, headers=headers)
    image_list = json.loads(response.text)
    return base64.b64decode(image_list[0])

if __name__ == "__main__":
    prompt = inputTransformer('sad angry red and black logo of eye')
    image_one = fetchColab(prompt, 1)
    image = outputTransformer(image_one)