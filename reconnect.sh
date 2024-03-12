while true
     do
     i=$(cat /sys/class/net/wlan1/carrier)
if [ $i == 1 ]
then
       echo "connected"

else
       echo "reconnecting"
       killall wpa_supplicant
       modprobe -rv rt2800usb
       modprobe -v rt2800usb
       wpa_supplicant -i wlan1 -c/etc/wpa_supplicant.conf -B
       dhclient wlan1
       echo "reconnected successfully"
       fi
sleep 10
done