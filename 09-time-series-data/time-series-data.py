import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('fivethirtyeight')

data = pd.read_csv('./data.csv')
data['Date']=pd.to_datetime(data['Date'])
data.sort_values('Date',inplace=True)
price_date=data['Date']
price_close=data['Close']



plt.plot_date(price_date,price_close, linestyle='solid',
              color='green', alpha=0.56, linewidth=0.8, )

plt.gcf().autofmt_xdate()


#
plt.title("Bitcoin Prices")
plt.xlabel('Dates')
plt.ylabel('Price at closing')
plt.tight_layout()
plt.show()



#dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]
#
# y = [0, 1, 3, 4, 6, 5, 7]