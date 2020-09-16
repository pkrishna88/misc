# checkin the battery %

import psutil
battery = psutil.sensors_battery()
print("Battery Percent: {}%".format(battery.percent))

