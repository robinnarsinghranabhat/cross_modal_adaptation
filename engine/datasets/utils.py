import os
import torch
import torchvision
from torchvision.datasets.folder import default_loader
from engine.datasets import dataset_classes
from engine.tools.utils import load_json
from imagenet_c import corrupt


def get_few_shot_setup_name(train_shot, seed):
    """Get the name for a few-shot setup.
    """
    return f"shot_{train_shot}-seed_{seed}"


class TextTensorDataset(torch.utils.data.Dataset):
    def __init__(self, input_tensor, label_tensor, eot_indices):
        self.input_tensor = input_tensor
        self.label_tensor = label_tensor
        self.eot_indices = eot_indices
    
    def __getitem__(self, index):
        return self.input_tensor[index], self.label_tensor[index], self.eot_indices[index]

    def __len__(self):
        return self.input_tensor.size(0)


class TensorDataset(torch.utils.data.Dataset):
    def __init__(self, input_tensor, label_tensor):
        self.input_tensor = input_tensor
        self.label_tensor = label_tensor
    
    def __getitem__(self, index):
        return self.input_tensor[index], self.label_tensor[index]
    
    def __len__(self):
        return self.input_tensor.size(0)

import numpy as np
from PIL import Image

class DatasetWrapper(torch.utils.data.Dataset):

    def __init__(self, data_source, transform, cmd_args=None):
        self.data_source = data_source
        self.transform = transform
        self.cmd_args = cmd_args

    def __len__(self):
        return len(self.data_source)

    def __getitem__(self, idx):
        item = self.data_source[idx]

        img = default_loader(item['impath'])
        ## Use noise=Corrupted
        if self.cmd_args.noise_type:
            crpt_img = corrupt( np.array(img, dtype=np.uint8), severity=2, corruption_name=self.cmd_args.noise_type )
            img = Image.fromarray(crpt_img)
            
        img = self.transform(img)

        output = {
            "img": img,
            "label": item['label'],
            "classname": item['classname'],
            "impath": item['impath'],
        }

        return output


def get_few_shot_benchmark(data_dir,
                           indices_dir,
                           dataset,
                           train_shot,
                           seed,
                           noise=""):
    # Check if the dataset is supported
    assert dataset in dataset_classes
    few_shot_index_file = os.path.join(
        indices_dir, dataset, f"{get_few_shot_setup_name(train_shot, seed)}.json")
    assert os.path.exists(few_shot_index_file), f"Few-shot data does not exist at {few_shot_index_file}."
    

    few_shot_dataset = load_json(few_shot_index_file)
    benchmark_class = dataset_classes[dataset]
    # Change the Path to load the dataset.
    # We assume a noise-corrupted folder is present.
    # if noise:
    #     benchmark_class.dataset_name += f"_{noise}"
        # Update the paths in few_shot_dataset ? 
        # Example : ./data/oxford_flowers/jpg/image_07870.jpg > ./data/oxford_flowers_gn/jpg/image_07870.jpg


    benchmark = benchmark_class(data_dir)
    return {
        'train': few_shot_dataset['train']['data'],
        'val': few_shot_dataset['val']['data'],
        'test': benchmark.test,
        'lab2cname': benchmark.lab2cname,
        'classnames': benchmark.classnames,
    }


def get_testset(dataset, data_dir):
    if dataset in dataset_classes:
        benchmark = dataset_classes[dataset](data_dir)
        return benchmark.test
    else:
        raise NotImplementedError()


def get_label_map(data_dir, dataset_name):
    if dataset_name in ['imagenet_a', 'imagenet_r']:
        benchmark = dataset_classes[dataset_name](data_dir)
        return benchmark.label_map
    else:
        return None