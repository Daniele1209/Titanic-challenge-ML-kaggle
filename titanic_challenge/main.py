import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data_train = pd.read_csv("train.csv")
print("Train data head:\n", data_train.head(9))

