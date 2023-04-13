echo "Installing sway, please wait.."
dnf install -y sway


echo "Installing sway components, please wait.."
dnf install -y foot waybar wofi light


echo "Setting up configurations, please wait.."
cp -r /home/sarthak/dotfiles/foot /home/sarthak/.config/
cp -r /home/sarthak/dotfiles/sway /home/sarthak/.config/
cp -r /home/sarthak/dotfiles/waybar /home/sarthak/.config/
cp -r /home/sarthak/dotfiles/wofi /home/sarthak/.config/
