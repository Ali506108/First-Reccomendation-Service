import io
import zipfile
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader,Dataset
import requests

# 1. install MovieLens 100k
url = "https://files.grouplens.org/datasets/movielens/ml-100k.zip"
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))

ratings = pd.read_csv(
    z.open("ml-100k/u.data"),
    sep="\t",
    names=[
        "user_id",
        "movie_id",
        "rating",
        "timestamp"
    ]
)

movies = pd.read_csv(
    z.open("ml-100k/u.item"),
    sep="|",
    encoding="latin-1",
    header=None,
    usecols=[0,1],
    names=["movie_id","title"],
)


user_to_idx = {uid: i for i ,uid in enumerate(ratings["user_id"].unique())}
movie_to_idx = {mid: i for i , mid in enumerate(ratings["movie_id"].unique())}
idx_to_movie = {i: mid for mid , i in movie_to_idx.items() }

ratings["user_idx"] = ratings['user_id'].map(user_to_idx)
ratings["movie_idx"] = ratings['movie_id'].map(movie_to_idx)

num_users = len(user_to_idx)
num_movies = len(movie_to_idx)
global_mean = ratings["ratings"].mean()

print(f"Users : {num_users}\nMovies: {num_movies}\ngloabl mean is : {global_mean}")
