#!/bin/bash
installdir=~/848-P2P-Chat
sudo apt install dialog
dialog --title "848 P2P Chat Installer" --clear --msgbox "Welcome to the 848 P2P Chat Insaller, to proceed press ENTER, to abort press ESC." 16 51
dialog --title "848 P2P Chat Installer" --clear --msgbox "First we will update the package archives, then we will install the prerequisites." 16 51

sudo apt update

sudo apt install pyqt4-dev-tools
sudo apt install python-qt4
sudo apt install python3-qt4
sudo apt install qt-designer
sudo apt install git
cd ~
cd "$installdir" || {
dialog --title "848 P2P Chat Installer" --clear --msgbox "Cloning from GitHub..." 16 51

git clone https://github.com/GamerMole21/848-P2P-Chat.git
cd 848-P2P-Chat
chmod +x chat4.py
dialog --title "848 P2P Chat Installer" --clear --msgbox "848 P2P Chat successfully installed." 16 51
exit
}
dialog --title "848 P2P Chat Installer" --clear --msgbox "848 P2P Chat was already installed."
