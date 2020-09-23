# RaspberryPiKernelEncoder

Tested on Rasbian Buster

Software Initial Setup:
- sudo apt-get -y install raspberrypi-kernel-headers
- If that doesn't work do:
	- sudo apt-get -y install --reinstall raspberrypi-bootloader raspberrypi-kernel raspberrypi-kernel-headers


Compiling and installing kernel driver:
- Go to the repo's directory
- make  (compiles kernel module)
- sudo make load (installs kernel module)
- sudo make unload (remove kernel module)

Electrical Hookup:
- Pin number definitions in device_file.c
- Change pin definitions at your own risk.  Changes sometimes interfere with other interrupts and cause the driver not to work properly.
- I tested 2x simulated encoders at 12kHz with an FPGA.  About 3-5% CPU usage on a Raspberry Pi Zero W (didn't test other Raspberry Pis but it should work).
- Pin numbers Encoder 1
	- A - 17, B - 27
- Encoder 2
	- A - 5, B - 6
- Encoder 3
	- A - 23, B - 24
- Encoder 4
	- A - 16, B - 26


Testing:
- test.c prints out encoder counts
	- gcc -i test.c -o test (then sudo ./test to run)
- reset.c resets encoder counts by writing to char driver in /dev
	- gcc -i reset.c -o reset (then sudo ./reset to run)


Usage:
- sudo make load creates a device driver /dev/encoder-driver
	- To read the counts, simply read sizeof(int) * 4 bytes from the driver.  Those will be the counts for the four encoder channels in binary (cast to int to read)  No matter what you read, it will always return that number of bytes.
	- To reset the counts, write anything to the driver
