import gpt_2_simple as gpt2
import tensorflow as tf
import os

model_name = "124M"
#tf.reset_default_graph()
#if not os.path.isdir(os.path.join("models", model_name)):
#    print(f"Downloading {model_name} model...")
#    gpt2.download_gpt2(model_name=model_name)  # model is saved into current directory under /models/124M/

file_name = "./meta_context.csv"

sess = gpt2.start_tf_sess()

#gpt2.finetune(sess,
#            dataset=file_name,
#            model_name=model_name,
#            steps=1000, sample_every=40, print_every=10, save_every=10)  # steps is max number of training steps


gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              multi_gpu=True,
              steps=1000, save_every=10)  # steps is max number of training steps
#
gpt2.generate(sess)
