import numpy as np
import pandas as pd

import os
for dirname, _, filenames in os.walk('/data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

data = pd.read_csv("train.csv")
print("Train data head:\n", data.head(9))

