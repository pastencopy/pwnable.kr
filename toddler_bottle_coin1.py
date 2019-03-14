import string
import socket

'''
pwnable.kr challenge

toddler's bottle > coin1


nc 0 9007

'''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',9007))

ONE_WEIGHT = 10

recvdata = sock.recv(10000)
print(recvdata)
#It will be run after 3 secound

#step 0 to 99 , Loop for 100 times
for i in range(0,100):
    
    recvdata = sock.recv(1024)
    arg = recvdata.split()

    n = int(arg[0].split('=')[1])
    c = int(arg[1].split('=')[1])

    print('[<]n=' + str(n) + ', c='+str(c) + '\n')

    left = 0
    right = n

    found = -1
    
    while (1):

        mid = left + ((right - left)/2)
        
        if (left == mid) :
                mid = right

        senddata = ''
        
        if (found >= 0) :
            #Repeat for 'c' times
            senddata = str(found)
        else:
            for num in range(left,mid):
                senddata += str(num)+' '

        print('[>]Send : ' + senddata + '\n')
        sock.send(senddata+'\n')
        recvdata = sock.recv(1024)
        '''
        #Check Weight
        print('[<] weight=' + recvdata + ', target_weight=' + str((mid - left) * ONE_WEIGHT))
        '''
        
        if recvdata.find('Correct') >= 0 :
            #Correct, Go to Next Loop!
            print('[+]Correct : ' + str(i) +'\n')
            break
        elif recvdata.find('Wrong') >= 0 :
            #Binary Search Failed.
            #I think it will be not happen ever.... :D
            print('[-]Wrong Coin Detected!! : ' + str(i) + '\n')
            break

        if (int(recvdata) < ONE_WEIGHT) :
            found = int(senddata)
            print('[+]Coin Found! : ' + str(found) +'\n')            
        else:
            #Binary Search!
            if ((mid - left) * ONE_WEIGHT == int(recvdata)):
                left = mid
            else:
                right = mid

#Print Final Message
recvdata = sock.recv(10000)
print(recvdata)

sock.close()
