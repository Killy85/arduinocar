# arduinocar

This is a raspberry python programm which will use bluetooth to connect to an arduino and send data over a BLE adapter.

## Troubleshoting

If you face the following problem :

`Failed to execute management command 'le on' (code: 20, error: Permission Denied)`

It may be because your python exe is not allowed to run the bluetooth firmware.

You may type `sudo setcap 'cap_net_raw,cap_net_admin+eip' PATH/TO/LIB/python3.5/site-packages/bluepy/bluepy-helper` to correct it 
. You may also run the programm with `sudo` but it may create problem with librarys.
