#! /bin/bash
apt -y install raspberrypi-kernel-headers
apt -y install --reinstall raspberrypi-bootloader raspberypi-kernel raspberrypi-kernel-headers
sudo -u pi make
sudo make load
