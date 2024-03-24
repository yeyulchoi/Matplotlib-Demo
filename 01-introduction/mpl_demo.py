from matplotlib import pyplot as plt


plt.style.use('ggplot')

# plt.xkcd()


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, linestyle='-', color='c', label='JS')

# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x, dev_y, color='k', linestyle='--',marker='.' ,label='All Devs')




# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x,py_dev_y,'-r', label='Python', linewidth=4)

plt.xlabel('Age')
plt.ylabel('Salary')
plt.title("Median  Developer Salaries by Age")


# plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig('01-introduction/plot.png')

plt.show(block=True)
