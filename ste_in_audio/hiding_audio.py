import wave

import numpy as np
import run_lenght
import Encrypt_DES


# string1 = input('Enter a message: ')
# def case(a):
#     if a == 1:
#         encode()
#     elif a == 2:
#         decode()
#     elif a == 3:
#         quit()
#     else:
#         print("\nEnter valid Choice!")

def encoded_hiding_audio(source_path, message, pwd, out_path):
    print("\nEncoding Starts..")
    try:
        audio = wave.open(source_path,mode="rb")
    except IOError:
        print("File not accessible")
        return False
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    string = run_lenght.encode_message(message)
    print(string)

    cipher_text = str(Encrypt_DES.encryptDES(string,pwd))
    print(cipher_text)
    cipher_text = cipher_text + int((len(frame_bytes)-(len(cipher_text)*8*8))/8) *'#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in cipher_text])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254)|bit
    frame_modified1 = bytes(frame_bytes)
    try:
        newAudio =  wave.open(out_path, 'wb')
    except IOError:
        print("File not accessible")
        return False
    newAudio.setparams(audio.getparams())
    newAudio.writeframes(frame_modified1)

    newAudio.close()
    audio.close()
    print(" |---->succesfully encoded inside",out_path)
    return True

def decoded_hiding_audio(audio_src, pwd, messages_file_des):
    print("\nDecoding Starts..")
    try:
        audio = wave.open(audio_src, mode='rb')
    except IOError:
        print("File not accessible")
        return False
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    decoded = string.split("###")
    messages = decoded[0]
    messages = Encrypt_DES.decryptDES(messages.encode(),pwd)
    # Xử lý dấu cách 2 đầu chuỗi
    messages = messages.strip()
    plantext = run_lenght.decode_mess(messages)


    print("Sucessfully decoded: "+ plantext)
    try:
        messages_file = open(messages_file_des,'w')
    except IOError:
        print("File not accessible")
        return False
    messages_file.write(plantext)
    
    messages_file.close()
    audio.close()	
    return True

def PSNR_Audio(original, modified):
    #print(len(original), len(modified))
    maximum = 255
    size = len(original)
    MSE = np.sum(pow(original[i] - modified[i], 2) for i in range(size))/size
    if MSE == 0:
        print("no has psnr")
        quit()
    else:
        PSNR = 10*np.log10(maximum*maximum/MSE)
        return PSNR
        
# while(1):
#     print("\nSelect an option: \n1)Encode\n2)Decode\nPress anything to quit")
#     val = int(input("\nChoice:"))
#     case(val)