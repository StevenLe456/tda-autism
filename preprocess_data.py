import networkx as nx
import os
import pandas as pd
import pickle

df = pd.read_csv("phenotype.csv")

with open("AAL.txt") as f:
    raw_str = f.read()

brain_regions = {i // 2 + 1: s for i, s in enumerate(raw_str.split()) if i % 2 == 1}

subj = {}

for root, dirs, files in os.walk("ABIDEII-connectomes"):
    for f in files:
        filepath = os.path.join(root, f)
        if filepath.find("AAL_space-") + 1:
            subj[int(filepath[filepath.index("sub-") + 4 : filepath.index("sub-") + 9])] = filepath

subj_dict = {}

for subid, s in subj.items():
    temp = {}
    g = nx.to_dict_of_dicts(nx.read_weighted_edgelist(s, create_using=nx.DiGraph))
    p = df.loc[df["SUB_ID"] == subid].squeeze().to_dict()
    temp["graph"] = g
    temp["phenotype"] = p
    subj_dict[subid] = temp

with open("subjects.pickle", "wb") as p:
    pickle.dump(subj_dict, p)