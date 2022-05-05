from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw
import os
import json
import requests
import base64
# from docarray import Document

def inputTransformer(input_text=None):
    file_name = 'input.txt'
    # full_path = os.path.join(input_path, file_name)
    # input_text = input_text or 'logo big green tree in circle'
    # print(full_path, 'full_path')

    # if not os.path.exists(input_path):
    #     os.makedirs(input_path)
    #     print('directory is created!', input_path)

    # with open(file_name, 'w') as f:
    #     if os.path.getsize(file_name) == 0:
    #         f.write(input_text)

    readme = open(file_name,'r')
    readme_text = readme.read()
    readme.close()
    print(readme_text, 'readme_text')
    return readme_text


def outputTransformer(image=None):
    output_path = 'output/'
    image_name = 'icon.png'
    full_output_path = os.path.join(output_path, image_name)

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print("The new directory is created!", output_path)
    with open(full_output_path, 'wb') as f:
        f.write(image)

    # im = ImageEnhance.Color(im).enhance(5.0)
    # im = ImageOps.posterize(im, 2)
    im = Image.open(full_output_path).convert("L")
    # im = ImageEnhance.Brightness(im).enhance(1.2)
    # im = ImageOps.autocontrast(im, cutoff=0, ignore=None, mask=None, preserve_tone=True)
    im = ImageOps.autocontrast(im)
    im = ImageEnhance.Contrast(im).enhance(5.0)
    
    # colors = open('colors.json')
    colors = json.load(open('colors.json'))
    print(colors['contrastAdjusted'], colors['primary'])
    im = ImageOps.colorize(im, black = colors['contrastAdjusted'], white=colors['primary'], mid=colors['primary'], 
        blackpoint=50,  whitepoint=200,  midpoint=100)
    

    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, resample=Image.Resampling.LANCZOS)
    im.putalpha(mask)
    # Matrix = ( 1.1, 0,  0, 0, 0,   0.9, 0, 0, 0,     0, 1, 0) 
    # im = im.convert("RGBA", MATRIX)
    im = ImageOps.expand(im, border=5, fill=10)
    datas = im.getdata()
    # Create transparency
    im = im.convert("RGBA")
    newData = []
    for item in datas:
        if item[0] >= 200 and item[1] >= 200 and item[2] >= 200:  # findingblack color by its RGB value
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)  # other colours remain unchanged
    im.putdata(newData)

    im = im.filter(ImageFilter.GaussianBlur(radius = 1))
    im.save("output/icon.png", "PNG")


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

# from docarray import Document
# def fetchMega(prompt, num_images):
#   # run installer for this function
#   # !pip install "docarray[common]>=0.13.5" jina
#   server_url = 'grpc://dalle-flow.jina.ai:51005'
#   da = Document(text=prompt).post(server_url, parameters={'num_images': num_images}).matches
#   # da.plot_image_sprites(fig_size=(3,3), show_index=True)
#   fav_id = 0
#   fav = da[fav_id]
#   diffused = fav.post(f'{server_url}/diffuse', parameters={'skip_rate': 0.5}, target_executor='diffusion').matches
#   # diffused.plot_image_sprites(fig_size=(5,5), show_index=True)
#   dfav_id = 0
#   fav = diffused[dfav_id]
#   # fav = fav.post(f'{server_url}/upscale', target_executor='upscaler')
#   fav.display()

def fetchColab(prompt, num_images):
    url = 'https://chubby-groups-tell-35-189-160-197.loca.lt/dalle'
    payload = setData(prompt, num_images)
    headers = setHeaders()
    response = requests.post(url, json=payload, headers=headers)
    image_list = json.loads(response.text)
    return base64.b64decode(image_list[0])

if __name__ == "__main__":
    prompt = inputTransformer()
    image_one = fetchColab(prompt, 1)
    image = outputTransformer(image_one)