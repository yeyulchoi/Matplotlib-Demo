from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')


days=[1,2,3,4,5,6,7,8,9]


player1 = [5, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [2, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [1, 1, 1, 1, 2, 2, 3, 3, 4]


labels=["player1","player2","player3"]
colors=['#FF71CD', '#5755FE','#8B93FF']
plt.stackplot( days, player1, player2, player3, labels=labels, colors=colors)


# plt.legend(loc="lower left" )
plt.legend(loc=(0.07, 0.05))

plt.title('My Stack Plot')
plt.tight_layout()
plt.show()