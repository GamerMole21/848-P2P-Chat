#!/bin/bash
sudo apt install dialog
dialog --title "848 P2P Chat Installer" --clear --yesno "Welcome to the 848 P2P Chat Insaller, are you ready to proceed?"
dialog --title "848 P2P Chat Installer" --clear --msgbox "First we will update the package archives, then we will install the prerequisites."
sudo apt update
sudo apt install pyqt4-dev-tools python-qt4 python3-qt4 qt-designer git
cd ~
if [ ! -d "848-P2P-Chat"]; then
  dialog --title "848 P2P Chat Installer" --clear --msgbox "Cloneing from GitHub..."
  git clone https://github.com/GamerMole21/848-P2P-Chat.git
  cd 848-P2P-Chat
  chmod +x chat4.py
  dialog --title "848 P2P Chat Installer" --clear --msgbox "848 P2P Chat successfully installed."
fi
dialog --title "848 P2P Chat Installer" --clear --msgbox "848 P2P Chat is already installed."
