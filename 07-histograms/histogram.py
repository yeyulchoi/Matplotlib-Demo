import pandas as pd
from matplotlib import pyplot as plt


plt.style.use('ggplot')
data = pd.read_csv('./data.csv')
ids = data['Responder_id']
ages= data['Age']

bins =[10,20,30,40,50,60,70,80,90,100]
plt.hist(ages, bins =bins, edgecolor="white", log=True)

median_age =29
color = '#007F73'

plt.axvline(median_age,color=color, label='Age Median', linewidth=3)

plt.xlabel('Ages')
plt.ylabel('Respondents')

plt.title("Histogram")

plt.tight_layout()
plt.show()