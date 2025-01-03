!pip install fastai --upgrade
from fastai.vision.all import *
path=untar_data(URLs.PETS)
fnames = get_image_files(path/'images')
pat = r'(.+)_\d+.jpg$'

batch_tfms = [*aug_transforms(size=224, max_warp=.9), Normalize.from_stats(*imagenet_stats)]
item_tfms = RandomResizedCrop(460, min_scale=0.75, ratio=(1.,1.))
bs=64
dls = ImageDataLoaders.from_name_re(path, fnames, pat, batch_tfms=batch_tfms, 
                                   item_tfms=item_tfms, bs=bs)
print(f"Number of classes: {dls.c}, class names: {dls.vocab}")
print(f"Images in train set: {len(dls.train.dataset)}")
print(f"Images in validation set: {len(dls.valid.dataset)}")
dls.show_batch()
dls.train.show_batch()
dls.valid.show_batch()
learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(2,3e-3)
learn.show_results()
from fastai.vision.all import *
path=untar_data(URLs.PETS)
fnames = get_image_files(path/'images')
pat = r'(.+)_\d+.jpg$'

batch_tfms = [*aug_transforms(size=224, max_warp=.9), Normalize.from_stats(*imagenet_stats)]
item_tfms = RandomResizedCrop(460, min_scale=0.75, ratio=(1.,1.))
bs=64
dls = ImageDataLoaders.from_name_re(path, fnames, pat, batch_tfms=batch_tfms, 
                                   item_tfms=item_tfms, bs=bs)
print(f"Number of classes: {dls.c}, class names: {dls.vocab}")
print(f"Images in train set: {len(dls.train.dataset)}")
print(f"Images in validation set: {len(dls.valid.dataset)}")
dls.show_batch()
dls.train.show_batch()
dls.valid.show_batch()
learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(2,3e-3)
learn.show_results()
