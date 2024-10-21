import os
import pandas as pd

df = pd.read_csv("phenotype.csv")

with open("AAL.txt") as f:
    raw_str = f.read()

brain_regions = {i // 2 + 1: s for i, s in enumerate(raw_str.split()) if i % 2 == 1}

list_of_files = []

for root, dirs, files in os.walk("ABIDEII-connectomes"):
    for f in files:
        filepath = os.path.join(root, f)
        if filepath.find("AAL_space-") + 1:
            list_of_files.append(filepath)

