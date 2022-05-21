import bpcs

alpha = 0.45
vslfile = 'logo.png'
msgfile = 'message1.txt' # can be any type of file
encfile = '.encoded.png'
msgfile_decoded = 'tmp.txt'

bpcs.capacity(vslfile, alpha) # check max size of message you can embed in vslfile
bpcs.encode(vslfile, msgfile, encfile, alpha) # embed msgfile in vslfile, write to encfile
#bpcs.decode(encfile, msgfile_decoded, alpha) # recover message from encfile