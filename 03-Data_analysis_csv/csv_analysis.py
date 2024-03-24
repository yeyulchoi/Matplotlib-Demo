import csv
import numpy as np
from matplotlib import pyplot as plt

# plt.style.use('fivethirtyeight')


with open('./data82.csv') as file:
    csv_reader = csv.DictReader(file)
    
    row = next(csv_reader)
    print(row)
    


# plt.title('')
# plt.xlabel('Ages')
# plt.ylabel('Salary')


# plt.tight_layout()
# plt.show()