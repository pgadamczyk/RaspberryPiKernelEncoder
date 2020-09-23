# get the name of the driver to make the char device.
grep "encoder-driver" /proc/devices | grep "[0-9]*" -oh
