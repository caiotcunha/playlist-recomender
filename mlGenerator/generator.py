from fpgrowth_py import fpgrowth
import pandas as pd
import pickle
import os
import ssl
from datetime import datetime
ssl._create_default_https_context = ssl._create_unverified_context

datapath = os.getenv("DATASET")

dataset = pd.read_csv(datapath)

playlist_list = dataset.groupby('pid')['track_name'].apply(list).tolist()

freqItemSet, rules = fpgrowth(playlist_list, minSupRatio=0.1, minConf=0.5)

metadata = {
    "rules": rules,
    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}


#for rule in rules[:5]:
#    antecedent, consequent, confidence = rule
#    print(f"{antecedent},{consequent},{confidence:.2f}")

pickle.dump( metadata, open( "/data/model.pickle", "wb" ) )
