from sklearn.preprocessing import LabelEncoder, StandardScaler
from torch.utils.data import DataLoader, TensorDataset, Subset
from torchvision import transforms, datasets
import torch
import pandas as pd
import pickle
import os
import yaml

def transform_data(input_dir: str, output_dir: str, params: dict) -> None:
    
    transform = transforms.Compose([
        transforms.Resize(params['resize']),
        transforms.ToTensor(),
        transforms.Normalize(params['normalize'][0], params['normalize'][1])
    ])
    
    dataset = datasets.ImageFolder(root=input_dir, transform=transform)
    num_classes = len(dataset.classes)
    
    print(f"size: {len(dataset)}\nnum classes: {num_classes}\nclasses: {dataset.classes}")
    
    dataloader = DataLoader(dataset, batch_size=params['batch_size'], shuffle=True)
    
    with open(output_dir, 'wb') as f:
        pickle.dump(dataloader, f)
        
def main():
    os.makedirs(os.path.join("data", "features"), exist_ok=True)
    
    params = yaml.safe_load(open("params.yaml"))["features"]
    
    transform_data("data/splitted/train", "data/features/train.pkl", params)
    transform_data("data/splitted/test", "data/features/test.pkl", params)
    
if __name__ == "__main__":
    main()
        
    
        
    