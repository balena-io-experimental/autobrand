import gpt_2_simple as gpt2
import os

checkpoint_dir="./checkpoint"
input_artifact="./artifacts/prefix_file.txt"
output_artifact="./artifacts/prefix_and_suggestion.txt"
model_name = '124M'

# Get our text for suggestion
f = open(input_artifact, "r")
prefix_text = f.read()
f.close

# Need to clean up text if we don't have a tranformer

sess = gpt2.start_tf_sess()
# After 3 hours of debugging I have realised that you need to put also the checkpoint_dir under generate.

gpt2.load_gpt2(sess,
              run_name='run1',
              checkpoint_dir=checkpoint_dir,
              model_name=model_name,
              model_dir='models',
              )

single_name = gpt2.generate(sess, model_name=model_name,
              run_name='run1', checkpoint_dir=checkpoint_dir,
              return_as_list=True,
              temperature=4, include_prefix=True, prefix=prefix_text,
              truncate='<|endoftext|>', nsamples=1, batch_size=1, length=3
              )[0]

# print(single_name)

if os.path.exists(output_artifact):
    os.remove(output_artifact)
f = open(output_artifact, "w")
f.write(single_name)
f.close()