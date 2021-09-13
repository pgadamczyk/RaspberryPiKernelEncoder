#! /bin/bash
git clone https://github.com/jtabor/RaspberryPiKernelEncoder.git
apt -y install raspberrypi-kernel-headers
apt -y install --reinstall raspberrypi-bootloader raspberypi-kernel raspberrypi-kernel-headers
cd RaspberryPiKernelEncoder
sudo -u pi make
sudo make load
