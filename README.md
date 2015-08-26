# pylibC95HF
linux python wrapper for CR95HF nfc lib

Still work in progress..
Added a Makefile to the original code.

Didn't find license agreement for STMicroelectronics

To get user access to the CR95HF make sure to put the 60-CR95HF.rules in your /etc/udev/rules.d folder
(remember that the default-hid.rules start at 50 so go bigger to overwrite the default)
Read_Block and Write_Block functions don't @myplace (use STCmd)

###Todo
- See [issues]:https://github.com/profOnno/pylibCR95HF/issues

###other things
to get the symbols from the libCR95HF.so
`nm -g libCR95HF.so`

