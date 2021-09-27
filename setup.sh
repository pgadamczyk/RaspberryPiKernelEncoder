#! /bin/bash
git clone https://github.com/jtabor/RaspberryPiKernelEncoder.git
sudo chown -R pi RaspberryPiKernelEncoder
apt -y install raspberrypi-kernel-headers
apt -y install --reinstall raspberrypi-bootloader raspberrypi-kernel raspberrypi-kernel-headers
cd RaspberryPiKernelEncoder
sudo -u pi make
sudo make load
