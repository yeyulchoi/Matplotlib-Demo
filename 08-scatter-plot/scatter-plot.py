from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('_mpl-gallery')




labels=['Viewers', 'Likes']
data= pd.read_csv('./data.csv')
view_count= data['view_count']
likes = data['likes']
ratio = data['ratio']

# plt.scatter(view_count,likes)
plt.scatter(view_count,likes, cmap='summer', c=ratio, edgecolor='black' , alpha=0.75 , linewidth=1)

plt.xscale('log')
plt.yscale('log')
cbar =plt.colorbar()
cbar.set_label('Satisfaction degree')

plt.xlabel('View Counts')
plt.ylabel('Likes')



plt.title("Trending Youtube Videos")
# plt.lengend()
plt.tight_layout()  # automatic padding
plt.show()

