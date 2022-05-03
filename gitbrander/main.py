from PIL import Image
import os

###############
# READ input 
###############
input_path = 'input'
file_name = 'README.md'
full_path = os.path.join(input_path, file_name)
input_text = 'big green tree logo'
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


###############
# SAVE output
###############
output = 'output/'
if not os.path.exists(output):
  os.makedirs(output)
  print("The new directory is created!", output)

# Create new Image
img = Image.new(mode="RGB", size=(64, 64), color = (153, 153, 255))

# Convert to transparent
rgba = img.convert("RGBA")
datas = rgba.getdata()
  
newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
        # storing a transparent value when we find a black colour
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)  # other colours remain unchanged
  
rgba.putdata(newData)
rgba.save("output/logo.png", "PNG")