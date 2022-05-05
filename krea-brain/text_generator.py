import gpt_2_simple as gpt2
import os
import nltk

# This stuff helps remove stop words
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize

checkpoint_dir="./checkpoint"
input_artifact="./artifacts/prefix_file.txt"
output_artifact="./artifacts/suggestion.txt"
model_name = '124M'

# Get our text for suggestion
f = open(input_artifact, "r")
prefix_text_raw = f.read()
f.close

# 
# Need to clean up text if we don't have a tranformer
prefix_text_tokens = word_tokenize(prefix_text_raw)
prefix_text_tokens_without_sw = [word for word in prefix_text_tokens if not word in stopwords.words()]

prefix_text = (" ").join(prefix_text_tokens_without_sw)
prefix_text = prefix_text + "::"

# print("Clean text:", prefix_text)


sess = gpt2.start_tf_sess()
# After 3 hours of debugging I have realised that you need to put also the checkpoint_dir under generate.

gpt2.load_gpt2(sess,
              run_name='run1',
              checkpoint_dir=checkpoint_dir,
              model_name=model_name,
              model_dir='models',
              )

results = gpt2.generate(sess, model_name=model_name,
              run_name='run1', checkpoint_dir=checkpoint_dir,
              return_as_list=True,
              temperature=4, include_prefix=True, prefix=prefix_text,
              truncate='<|endoftext|>', nsamples=1, batch_size=1, length=3
              )[0]

#print("=====================================")
#print(results)
#print("=====================================")
results_split = results.split("::", 1)
#print(results_split[1])
#print("=================================")

if os.path.exists(output_artifact):
    os.remove(output_artifact)
f = open(output_artifact, "w")
f.write(results_split[1])
f.close()