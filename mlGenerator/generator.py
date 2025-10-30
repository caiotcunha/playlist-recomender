from fpgrowth_py import fpgrowth
import pandas as pd
import pickle

datapath = "/home/datasets/spotify/2023_spotify_ds1.csv"

dataset = pd.read_csv(datapath)

playlist_list = dataset.groupby('pid')['track_name'].apply(list).tolist()

freqItemSet, rules = fpgrowth(playlist_list, minSupRatio=0.1, minConf=0.5)

pickle.dump( rules, open( "model.pickle", "wb" ) )
