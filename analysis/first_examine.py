import matplotlib.pyplot as plt

from utils import data_helper

path = '../data/aaa.csv'
data_frame = data_helper.read_data(path)
print data_frame.keys()

data_frame = data_frame[::-1]
OPEN_FIXED_KEY = "<OpenFixed>"
OPEN_KEY = "<Open>"
HIGH_FIXED_KEY = "<HighFixed>"
HIGH_KEY = "<High>"
LOW_FIXED_KEY = "<LowFixed>"
LOW_KEY = "<Low>"
CLOSE_FIXED_KEY = "<CloseFixed>"
CLOSE_KEY = "<Close>"
VOLUME_KEY = "<Volume>"
plt.plot(data_frame[OPEN_KEY])
plt.plot(data_frame[LOW_KEY])
plt.plot(data_frame[HIGH_KEY])
plt.plot(data_frame[CLOSE_KEY])
plt.show()
