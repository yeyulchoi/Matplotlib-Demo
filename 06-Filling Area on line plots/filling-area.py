from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
data = pd.read_csv('./data.csv')
ages= data['Age']
dev_salaries = data['All_Devs']
python_salaries = data['Python']
javascript_salaries = data['JavaScript']

plt.plot(ages,dev_salaries, linestyle='--', color='#FF71CD', label='All Devs')
plt.plot(ages,python_salaries, linestyle='-',color='#5755FE', label= 'Python Dev')
# plt.plot(ages,javascript_salaries, linestyle='-',color='#8B93FF', label='Javascript Dev')

overall_median = 57287
plt.fill_between(ages,python_salaries, dev_salaries,
                 where=(python_salaries > dev_salaries),
                interpolate=True,alpha=0.25,label="above average")


plt.fill_between(ages, python_salaries, dev_salaries, linestyle='-',
                 where=(python_salaries<=dev_salaries),
                 interpolate=True, color='pink' ,alpha=0.5, label="below average")






plt.tight_layout() # changing the padding line that help thing looks nicer
plt.legend()
plt.show()