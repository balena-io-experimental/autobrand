from PIL import Image
import os
import json
import requests
from docarray import Document

# !pip install "docarray[common]>=0.13.5" jina

def dalleMega():
  server_url = 'grpc://dalle-flow.jina.ai:51005'
  prompt = 'logo cheetah face in circle'
  da = Document(text=prompt).post(server_url, parameters={'num_images': 3}).matches
# da.plot_image_sprites(fig_size=(3,3), show_index=True)

  fav_id = 0
  fav = da[fav_id]
  diffused = fav.post(f'{server_url}/diffuse', parameters={'skip_rate': 0.5}, target_executor='diffusion').matches
# diffused.plot_image_sprites(fig_size=(3,3), show_index=True)
  dfav_id = 0
  fav = diffused[dfav_id]
  # fav = fav.post(f'{server_url}/upscale', target_executor='upscaler')
  fav.display()

dalleMega()