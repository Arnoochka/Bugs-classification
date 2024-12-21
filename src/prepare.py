import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from torchvision import datasets
import os
import yaml
import shutil


def prepare_data(split: float, seed: int):
    dataset_dir = "data/not_splitted"
    output_dir = "data/splitted"
    os.makedirs(output_dir, exist_ok=True
                )
    train_dir = os.path.join(output_dir, "train")
    test_dir = os.path.join(output_dir, "test")

    dataset = datasets.ImageFolder(root=dataset_dir)

    indices = list(range(len(dataset)))
    train_indices, test_indices = train_test_split(indices, test_size=split, random_state=seed)

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    for idx, target_dir in zip([train_indices, test_indices], [train_dir, test_dir]):
        for i in idx:
            source_path, label = dataset.samples[i]
            class_dir = os.path.join(target_dir, dataset.classes[label])
            os.makedirs(class_dir, exist_ok=True)

            dest_path = os.path.join(class_dir, os.path.basename(source_path))
            shutil.copy2(source_path, dest_path)
    
def main():
    params = yaml.safe_load(open("params.yaml"))["prepare"]

    split = params["split"]
    seed = params["seed"]
    prepare_data(split, seed)

if __name__ == '__main__':
    main()