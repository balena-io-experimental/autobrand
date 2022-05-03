from dalle_mini import DalleBart, DalleBartProcessor
from vqgan_jax.modeling_flax_vqgan import VQModel
from transformers import CLIPProcessor, FlaxCLIPModel
 
DALLE_MODEL = "dalle-mini/dalle-mini/wzoooa1c:latest" 
DALLE_COMMIT_ID = None
 
VQGAN_REPO = "dalle-mini/vqgan_imagenet_f16_16384"
VQGAN_COMMIT_ID = "e93a26e7707683d349bf5d5c41c5b0ef69b677a9"
 
CLIP_REPO = "openai/clip-vit-large-patch14"
CLIP_COMMIT_ID = None
 
model = DalleBart.from_pretrained(DALLE_MODEL, revision=DALLE_COMMIT_ID)
vqgan = VQModel.from_pretrained(VQGAN_REPO, revision=VQGAN_COMMIT_ID)
clip = FlaxCLIPModel.from_pretrained(CLIP_REPO, revision=CLIP_COMMIT_ID)
clip_processor = CLIPProcessor.from_pretrained(CLIP_REPO, revision=CLIP_COMMIT_ID)


# Defining image description

descript = "Dog wearing fancy hat"
tokenized_prompt = processor([descript])
tokenized_prompt = replicate(tokenized_prompt)
descript_1 = "Jupiter near the sun"
tokenized_prompt_1 = processor([descript_1])
tokenized_prompt_1 = replicate(tokenized_prompt_1)

# Generating image

from flax.training.common_utils import shard_prng_key
import numpy as np
from PIL import Image
from tqdm.notebook import trange
 
n_predictions = 10
gen_top_k = None
gen_top_p = None
temperature = 0.85
cond_scale = 3.0
 
images = []
for i in trange(max(n_predictions // jax.device_count(), 1)):
    key, subkey = jax.random.split(key)
    encoded_images = p_generate(
        tokenized_prompt,
        shard_prng_key(subkey),
        model.params,
        gen_top_k,
        gen_top_p,
        temperature,
        cond_scale,
    )
    encoded_images = encoded_images.sequences[..., 1:]
    decoded_images = p_decode(encoded_images, vqgan.params)
    decoded_images = decoded_images.clip(0.0, 1.0).reshape((-1, 256, 256, 3))
    for img in decoded_images:
        images.append(Image.fromarray(np.asarray(img * 255, dtype=np.uint8)))


print(f"Prompt: {descript}\n")
for idx in logits.argsort()[::-1]:
    display(images[idx])
    print(f"Score: {logits[idx]:.2f}\n")