import numpy as np
import pandas as pd
import torch
import transformers as ppb # pytorch transformers
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split


input = {
    "data_path": "C:/Users/EILON/PycharmProjects/data_set/traning/pan12-sexual-predator-identification-training-corpus-2012-05-01/pan12-sexual-predator-identification-training-corpus-2012-05-01",
}
json = open(input["data_path"] + ".json", encoding="utf8")
