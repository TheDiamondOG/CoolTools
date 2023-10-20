sudo pacman -S bluez bluez-utils blueman steam firefox git flatpak wine wine-mono wine-gecko clamtk discord chromium python3-pyqt5 python3-pip python3-pipx keepassxc code vlc libreoffice-fresh audacity openjdk gparted kcm-wacomtablet
pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
lsmod | grep btusb
sudo nano /etc/bluetooth/main.conf
sudo systemctl start bluetooth.service
sudo systemctl enable bluetooth.service
wine --version
sudo pacman -S
mkdir prism-launcher
cd prism-launcher
wgit https://github.com/PrismLauncher/PrismLauncher/releases/download/7.2/PrismLauncher-Linux-portable-7.2.tar.gz
tar -xf PrismLauncher-Linux-portable-7.2.tar.gz
rm -r -f PrismLauncher-Linux-portable-7.2.tar.gz
cd..
mkdir ExtraDownloadFiles
cd ExtraDownloadFiles
cd ..
yay -S lunar-client
flatpak install flathub org.zdoom.GZDoom
flatpak install flathub com.obsproject.Studio
flatpak install flathub com.github.iwalton3.jellyfin-media-player

sudo pacman -Sy
sudo pacman -Syy
sudo pacman -Syu
sudo pacman -Su
sudo pacman -Suu
