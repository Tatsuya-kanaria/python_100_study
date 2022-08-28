# %%
import yaml
import toml


# '''
# $cat config.yml
# dataset:
#   name: pseudo
#   path: data/images_by_py/
# use_gpu: true
# '''

with open('config.yml', mode='r') as f:
    config = yaml.safe_load(f)
config['dataset']

# '''
# $cat config.toml
# use_gpu = true

# [dataset]
# name = "pseudo"
# path = "data/images_by_py/"
# '''

with open('config.toml', mode='r') as f:
    config = toml.load(f)
config['dataset']['name']


# %%
