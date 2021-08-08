import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume,IAudioEndpointVolume

def get_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

def change_volume(option):
    volume=get_volume()
    if option==0:
        volume.SetMasterVolumeLevel(-50.0,None)
        return

    currentVolumeDb = volume.GetMasterVolumeLevel()
    print(currentVolumeDb)
    volume.SetMasterVolumeLevel(-22.0, None)
   
