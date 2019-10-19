import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# read data from online source
# tips = sns.load_dataset("https://github.com/mwaskom/seaborn-data/blob/master/tips.csv")

# reading locally stored tips data
tips = pd.read_csv("./../data/tips.csv")

sns.relplot(x="total_bill", y="tip", col="time",
            hue="smoker", style="smoker", size="size",
            data=tips)

plt.show()
