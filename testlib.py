#!/usr/bin/python
import pylibCR95HF.CR95HF as nfc

print nfc.USBConnect()
print nfc.Echo()
print nfc.MCUrev()
print nfc.getInterfacePinState()
print nfc.Idn()
print nfc.Select()
print nfc.SendReceive()
#print FieldOff()
print nfc.STCmd()
