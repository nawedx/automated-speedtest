import pandas as pd
import time
import datetime
import matplotlib.pyplot as plt 
import matplotlib
import matplotlib.dates as mdates
from pandas import ExcelWriter

#df = pd.DataFrame(columns=['Result_ID', 'Date', 'Time', 'Ping', 'Download_Speed', 'Upload_Speed', 'Server_Name', 'Server_Place', 'Result_URL'])

df = pd.read_excel('jio_speed_test.xls')

dt = df.Date+" "+df.Time
df.Download_Speed = df.Download_Speed.convert_objects(convert_numeric=True)
df.Upload_Speed = df.Upload_Speed.convert_objects(convert_numeric=True)
df['Result_ID'] = df['Result_ID'].fillna(0).astype(int)

print (df)
#print dt
ldr = [1.00]*195
print(ldr)
x=[]
x = [datetime.datetime.strptime(s, "%d-%m-%Y %H-%M") for s in dt]

downspeed = [s for s in df.Download_Speed]
#dn = [float(i) for i in downspeed]
upspeed = [s for s in df.Upload_Speed]

dates = matplotlib.dates.date2num(x)
print(dates)
plt.suptitle('Download speed trend of Jio 4G internet from 18th July 2018, 14:51 to 19th July 2018, 13:36 at (20.156720, 85.713394)', fontsize=16)
plt.plot_date(dates, downspeed, 'r-', label='Download Speed Trend')
plt.plot_date(dates, ldr, 'y-', label='1 Mbps')
plt.legend(loc='upper left')
#plt.plot_date(dates, upspeed, 'b-')
plt.xlabel('Timestamps of Speedtest (MM-DD HH)', fontsize=16)
plt.ylabel('Download Speed (Mbps)', fontsize=16)

#plt.axhline(y=1.00, label='Downspeed trend', color='yellow', linestyle='-')

'''
axes = plt.gca()
axes.set_xlim([xmin,xmax])
axes.set_ylim([0.00,15.0])
'''

plt.show()

plt.suptitle('Upload speed trend of Jio 4G internet from 18th July 2018, 14:51 to 19th July 2018, 13:36 at (20.156720, 85.713394)', fontsize=16)
#plt.plot_date(dates, downspeed, 'r-', label='Download Speed Trend')
plt.plot_date(dates, upspeed, 'b-', label='Upload Speed Trend')
plt.plot_date(dates, ldr, 'y-', label='1 Mbps')
plt.legend(loc='upper left')
plt.xlabel('Timestamps of Speedtest (MM-DD HH)', fontsize=16)
plt.ylabel('Upload Speed (Mbps)', fontsize=16)
plt.show()

plt.suptitle('Download and Upload speed trend of Jio 4G internet from 18th July 2018, 14:51 to 19th July 2018, 13:36 at (20.156720, 85.713394)', fontsize=16)
plt.plot_date(dates, downspeed, 'r-', label='Download Speed Trend')
plt.plot_date(dates, upspeed, 'b-', label='Upload Speed Trend')
plt.plot_date(dates, ldr, 'y-', label='1 Mbps')
plt.legend(loc='upper left')
plt.xlabel('Timestamps of Speedtest (MM-DD HH)', fontsize=16)
plt.ylabel('Download/Upload Speed (Mbps)', fontsize=16)
plt.show()

ax = plt.subplot(111)
ax.bar(dates, downspeed, width=0.0005)
ax.xaxis_date()
plt.axhline(y=1.00, color='yellow', linestyle='-')

plt.show()
