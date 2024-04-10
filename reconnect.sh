netGrep=$(cd /sys/class/net && echo *)
netName=$(cut -c 4- <<< $netGrep)

while true
     do
	i=$(cat /sys/class/net/$netName/carrier)
if [ $i == 1 ]
then
       echo "connected"

else
       echo "reconnecting"
       killall wpa_supplicant
       modprobe -rv rt2800usb
       modprobe -v rt2800usb
       wpa_supplicant -i $netName -c/etc/wpa_supplicant.conf -B
       dhclient $netName
       echo "reconnected successfully"
       fi
sleep 10
done
