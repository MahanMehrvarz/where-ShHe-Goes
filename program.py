
from utility import *

count=0
last_message=finding_last_message()
last_id=finding_last_id()

d1=5
d2=20
while True:
    location=get_location()    
    c=False
    a=False
    b=False
    d=False
    print location
    print "1st while"
    print "first location", location
    while last_id!=finding_last_id():
	print "2nd while"
        last_id=finding_last_id()
        n=finding_last_number()
        p_name=last_name() 
       
        if a==False and hello_check()==True : 
            first_message=finding_last_message()
            request=request_txt()
            sending_txt(request, n)
            time.sleep(d1)
            print request
            last_id=finding_last_id()
            a=True
            time.sleep(d2)
            

        elif a==False and hello_check()==False and d==False:
            #beaking the second while
            number=finding_last_number   
            coution="Do you wanna play? If yes please send me a hello followed by your name ;-)"
    	    sending_txt(coution, n)
            time.sleep(d1)
            print coution
            break
        
            
        if location!=get_location() and a==True and b==False and d==False:
            
            destination=get_location()
            print "destination got"
            reply="You think I should be in "+ destination +", awesome!"
            sending_txt(reply , n)
            time.sleep(d2)
            b=True
            count=1
	    location=get_location()
            

        elif location==get_location() and a==True and b==False and c==False:
            sending_txt(insist(), n)
            time.sleep(d1)
            print insist()
            print location
            #b=True
	    c=True
            time.sleep(d2)
        

        if location!=get_location() and a==True and b==False:
            first_location=location
            
            destination=get_location()
            reply="You think I should be in "+ destination +" awesome!"
            print "destination got "
            sending_txt(reply , n)
            time.sleep(d2)
            print 
            b=True
            count=1
            location=get_location()
        
        
        elif location==get_location() and a==True and b==False and c==True:
            
            #breaking the second loop
            babye="okay, bybye. ;-("
            sending_txt(babye, n)
	    print "okay, bybye. ;-("
	    break
	
	
        if location==get_location() and b==True:
            #breaking the second loop
            sending_txt(thanking(), n)
            sending_txt(thanking2(), n)

            print thanking()
            print thanking2()
            session_report="this number "+n+" ( "+ p_name +" )" +" moved the figure to "+ destination + " in response to "+"{ "+request+" }"
            f=open("report.txt", "a")
            f.write(session_report)
            f.write("\n")
            f.close()
            print session_report
 
            break

        print "end of 2nd loop"
        
