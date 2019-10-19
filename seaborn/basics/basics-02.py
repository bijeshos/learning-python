import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

# reading locally stored tips data
tips = pd.read_csv("./../../data/tips.csv")

# scatter plots
sns.relplot(x="total_bill", y="tip", data=tips)
plt.show()

sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)
plt.show()

sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker",
            data=tips)
plt.show()

sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips)
plt.show()

sns.relplot(x="total_bill", y="tip", hue="size", data=tips)
plt.show()

sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.75", data=tips)
plt.show()

sns.relplot(x="total_bill", y="tip", size="size", data=tips)
plt.show()

sns.relplot(x="total_bill", y="tip", size="size", sizes=(15, 200), data=tips)
plt.show()


# line plot
df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)
g.fig.autofmt_xdate()
plt.show()
