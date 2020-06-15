def browse():
    print("#########################################");
    i=0;
    global hindi;
    global kannada;
    global telugu;
    global movies;    
    hindi=["angrezi medium","kalank","zindagi na milegi dobaara"];
    kannada=["dia","love mocktail","odeya"];
    telugu=["sarilleru neekyavvaru","maharshi","dear commorade"];
    mov=["kannada","hindi","telugu"];
    print(".......WELCOME TO ONLINE TICKET BOOKING....... ");
    print("available movies in banglore!!");
    movies=hindi+kannada+telugu;
    tot=len(kannada)+len(hindi)+len(telugu);
    for i in range(0,tot):
        print(i+1,".",movies[i]);
    print(tot+1,"##OR## add filters");
    print(tot+2,"customer care :)");
    op=ascii(input("select your choice??:: "));
    print("press 1 to login or sign up\n press 2 to continue(if already signed up or logged in)");
    global pre;
    pre=int(input(""));
    
    key()

def key():
    if(pre==1):
        orcase()
    elif(pre==2):
        options()

def orcase():
    print("#########################################");
    print("press 1 to login");
    print("press any key to sign up");
    inp=int(input("enter the choice:: "));
    if(inp==1):
        login()
    else:
        signUp()
        
def options():
    conti()
    op=int(input("select your choice??:: "));
    if(op==1):
        angrez()
    elif(op==2):
        kalank()
    elif(op==3):
        zindagi()
    elif(op==4):
        dia()
    elif(op==5):
        lovmoc()
    elif(op==6):
        odeya()
    elif(op==7):
        sarnee()
    elif(op==8):
        maharshi()
    elif(op==9):
        decom()
    elif(op==10):
        filters()
    elif(op==11):
        print("customer care:: 6364304546 \n 9886954726");
    else:
        print("enter correct choice");
        
def filters():
    print("#########################################");
    print("languages available are:: \n 1.kannada \n 2.hindi \n 3.telugu");
    lang=int(input("how many languages do u need to filter:: "));
    if(lang==2):
        print("choose language you prefer:: \n 1.kannada and hindi");
        print("2.kannada and telugu \n 3.telugu and hindi ");
        cho=int(input("enter the choice:: "));
        if(cho==1):
            knh()
        elif(cho==2):
            knt()
        elif(cho==3):
            tnh()
    elif(lang==1):
        print("choose language you prefer:: \n 1.kannada \n 2.hindi \n 3.telugu");
        cho=int(input("enter the choice:: "));
        if(cho==1):
            print("results::");
            for i in range(0,len(kannada)):
                print(i+1,".",kannada[i]);
        elif(cho==2):
            print("results::");
            for i in range(0,len(hindi)):
                print(i+1,".",hindi[i]);
        elif(cho==3):
            print("results::");
            for i in range(0,len(telugu)):
                print(i+1,".",telugu[i]);            
           

def signUp():
    print("#########################################");
    print("        SIGN UP        ")
    email=ascii(input("email:: "));
    firstname=ascii(input("first Name:: "));
    lastname=ascii(input("last Name:: "));
    global username;
    username=ascii(input("username:: "));
    paswrd=ascii(input("password:: "));
    global existing_username,existing_password;
    existing_username=[];
    existing_password=[];    
    existing_username.append(username)
    existing_password.append(paswrd)
    print("succesfully registered")
    options()
    
def login():
    print("#########################################");
    print("LOGIN");
    username=ascii(input("enter the username:: "));
    password=ascii(input("enter the password:: "));
    for i in range(0,len(existing_password)):
        if(existing_username[i]==username and existing_password[i]==password):
            options()
        else:
            print("## the entered username or password is incorrect ##")
        login()

def angrez():
    print("**** ANGREZI MEDIUM ****");
    print("theatre:: rockline cinemas \n show-time:: 11:30am");
    print("review: XXXX")
    se=int(input("1.book ticket \n 2.rate and comment:: "));
    if(se==1):
        print("BOOKING TICKETS!!!")
        global seats;
        seats=int(input("enter the number of seats to be booked:: "));
        global totalSeats;
        totalSeats=[];
        for i in range(0,seats):
            num=int(input("enter the seat numbers::"));
            totalSeats.append(num);
        global amount;
        amount=seats*200;
        print("total amount to be paid:: ",amount);
        payop=int(input("payment options:\n1.UPI payment \n2.card:: "));
        if(payop==1):
            upi=ascii(input("enter UPI pin:: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: rockline cinemas \n show-time:: 11:30am");
                print("means of payment:: UPI payment");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()
        elif(payop==2):
            print("ADD CARD(all types of cards are accepted)");
            bana=ascii(input("Full name: "));
            carno=ascii(input("card number: "));
            expmon=ascii(input("expiry month: "));
            expdate=ascii(input("expiry date: "));
            cvv=ascii(input("cvv code: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: rockline cinemas \n show-time:: 11:30am");
                print("means of payment:: card");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()            
    else:
        rate=int(input("rate out of 10:: "));
        rt=[];
        rt.append(rate)
        for i in range(0,len(rt)):
            sum=0;
            sum=(sum+rt[i])/len(rt);
        com=[];
        cmt=ascii(input("comment:: "));
        com.append(cmt)
        for i in range(0,len(com)):
            print(username);
            print(com[i]);
            con=int(input("press 1 to continue browsing"));
            if(con==1):
                browse()            

def dia():
    print("**** DIA ****");
    print("theatre:: orian PVR \n show-time:: 9:00am");
    print("review: XXXX")
    se=int(input("1.book ticket \n 2.rate and comment:: "));
    if(se==1):
        print("BOOKING TICKETS!!!")
        global seats;
        seats=int(input("enter the number of seats to be booked:: "));
        global totalSeats;
        totalSeats=[];
        for i in range(0,seats):
            num=int(input("enter the seat numbers::"));
            totalSeats.append(num);
        global amount;
        amount=seats*180;
        print("total amount to be paid:: ",seats*180);
        payop=int(input("payment options:\n1.UPI payment \n2.card:: "));
        if(payop==1):
            upi=ascii(input("enter UPI pin:: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: orian PVR \n show-time:: 9:00am");
                print("means of payment:: UPI payment");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()
        elif(payop==2):
            print("ADD CARD(all types of cards are accepted)");
            bana=ascii(input("Full name: "));
            carno=ascii(input("card number: "));
            expmon=ascii(input("expiry month: "));
            expdate=ascii(input("expiry date: "));
            cvv=ascii(input("cvv code: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: orian PVR \n show-time:: 9:00am");
                print("means of payment:: card");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()                 
    else:
        rate=int(input("rate out of 10:: "));
        rt=[];
        rt.append(rate)
        for i in range(0,len(rt)):
            sum=0;
            sum=(sum+rt[i])/len(rt);
        com=[];
        cmt=ascii(input("comment:: "));
        com.append(cmt)
        for i in range(0,len(com)):
            print(username);
            print(com[i]);
            con=int(input("press 1 to continue browsing"));
            if(con==1):
                browse()            

def kalank():
    print("**** KALANK ****");
    print("theatre:: vaishnavi saphire PVR \n show-time:: 10:30pm");
    print("review: XXXX")
    se=int(input("1.book ticket \n 2.rate and comment:: "));
    if(se==1):
        print("BOOKING TICKETS!!!")
        global seats;
        seats=int(input("enter the number of seats to be booked:: "));
        global totalSeats;
        totalSeats=[];
        for i in range(0,seats):
            num=int(input("enter the seat numbers::"));
            totalSeats.append(num);
        global amount;
        amount=seats*220;
        print("total amount to be paid:: ",seats*220);
        payop=int(input("payment options:\n1.UPI payment \n2.card:: "));
        if(payop==1):
            upi=ascii(input("enter UPI pin:: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: vaishnavi saphire PVR \n show-time:: 10:30pm");
                print("means of payment:: UPI payment");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()
        elif(payop==2):
            print("ADD CARD(all types of cards are accepted)");
            bana=ascii(input("Full name: "));
            carno=ascii(input("card number: "));
            expmon=ascii(input("expiry month: "));
            expdate=ascii(input("expiry date: "));
            cvv=ascii(input("cvv code: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: vaishnavi saphire PVR \n show-time:: 10:30pm");
                print("means of payment:: card");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()                 
    else:
        rate=int(input("rate out of 10:: "));
        rt=[];
        rt.append(rate)
        for i in range(0,len(rt)):
            sum=0;
            sum=(sum+rt[i])/len(rt);
        com=[];
        cmt=ascii(input("comment:: "));
        com.append(cmt)
        for i in range(0,len(com)):
            print(username);
            print(com[i]);
            con=int(input("press 1 to continue browsing"));
            if(con==1):
                browse()            
    
def zindagi():
    print("**** ZINDAGI NA MILEGI DOBAARA ****");
    print("theatre:: orian PVR \n show-time:: 1:20pm");   
    print("review: XXXX")
    se=int(input("1.book ticket \n 2.rate and comment:: "));
    if(se==1):
        print("BOOKING TICKETS!!!")
        global seats;
        seats=int(input("enter the number of seats to be booked:: "));
        global totalSeats;
        totalSeats=[];
        for i in range(0,seats):
            num=int(input("enter the seat numbers::"));
            totalSeats.append(num);
        global amount;
        amount=seats*200;
        print("total amount to be paid:: ",seats*200);
        payop=int(input("payment options:\n1.UPI payment \n2.card:: "));
        if(payop==1):
            upi=ascii(input("enter UPI pin:: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: orian PVR \n show-time:: 1:20pm");
                print("means of payment:: UPI payment");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()
        elif(payop==2):
            print("ADD CARD(all types of cards are accepted)");
            bana=ascii(input("Full name: "));
            carno=ascii(input("card number: "));
            expmon=ascii(input("expiry month: "));
            expdate=ascii(input("expiry date: "));
            cvv=ascii(input("cvv code: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: orian PVR \n show-time:: 1:20pm");
                print("means of payment:: card");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()                
    else:
        rate=int(input("rate out of 10:: "));
        rt=[];
        rt.append(rate)
        for i in range(0,len(rt)):
            sum=0;
            sum=(sum+rt[i])/len(rt);
        com=[];
        cmt=ascii(input("comment:: "));
        com.append(cmt)
        for i in range(0,len(com)):
            print(username);
            print(com[i]);
            con=int(input("press 1 to continue browsing"));
            if(con==1):
                browse()            

def lovmoc():
    print("**** LOVE MOCKTAIL ****");
    print("theatre:: gayatri cinemas \n show-time:: 11:00pm");
    print("review: XXXX")
    se=int(input("1.book ticket \n 2.rate and comment:: "));
    if(se==1):
        print("BOOKING TICKETS!!!")
        global seats;
        seats=int(input("enter the number of seats to be booked:: "));
        global totalSeats;
        totalSeats=[];
        for i in range(0,seats):
            num=int(input("enter the seat numbers::"));
            totalSeats.append(num);
        global amount;
        amount=seats*150;
        print("total amount to be paid:: ",seats*150);
        payop=int(input("payment options:\n1.UPI payment \n2.card:: "));
        if(payop==1):
            upi=ascii(input("enter UPI pin:: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: gayatri cinemas \n show-time:: 11:00pm");
                print("means of payment:: UPI payment");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()
        elif(payop==2):
            print("ADD CARD(all types of cards are accepted)");
            bana=ascii(input("Full name: "));
            carno=ascii(input("card number: "));
            expmon=ascii(input("expiry month: "));
            expdate=ascii(input("expiry date: "));
            cvv=ascii(input("cvv code: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: gayatri cinemas \n show-time:: 11:00pm");
                print("means of payment:: card");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()                 
    else:
        rate=int(input("rate out of 10:: "));
        rt=[];
        rt.append(rate)
        for i in range(0,len(rt)):
            sum=0;
            sum=(sum+rt[i])/len(rt);
        com=[];
        cmt=ascii(input("comment:: "));
        com.append(cmt)
        for i in range(0,len(com)):
            print(username);
            print(com[i]);
            con=int(input("press 1 to continue browsing"));
            if(con==1):
                browse()            

def odeya():
    print("**** ODEYA ****");
    print("theatre:: maruti theatre \n show-time:: 3:40pm");
    print("review: XXXX")
    se=int(input("1.book ticket \n 2.rate and comment:: "));
    if(se==1):
        print("BOOKING TICKETS!!!")
        global seats;
        seats=int(input("enter the number of seats to be booked:: "));
        global totalSeats;
        totalSeats=[];
        for i in range(0,seats):
            num=int(input("enter the seat numbers::"));
            totalSeats.append(num);
        global amount;
        amount=seats*190;
        print("total amount to be paid:: ",seats*190);
        payop=int(input("payment options:\n1.UPI payment \n2.card:: "));
        if(payop==1):
            upi=ascii(input("enter UPI pin:: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: maruti theatre \n show-time:: 3:40pm");
                print("means of payment:: UPI payment");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()
        elif(payop==2):
            print("ADD CARD(all types of cards are accepted)");
            bana=ascii(input("Full name: "));
            carno=ascii(input("card number: "));
            expmon=ascii(input("expiry month: "));
            expdate=ascii(input("expiry date: "));
            cvv=ascii(input("cvv code: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: maruti theatre \n show-time:: 3:40pm");
                print("means of payment:: card");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()                
    else:
        rate=int(input("rate out of 10:: "));
        rt=[];
        rt.append(rate)
        for i in range(0,len(rt)):
            sum=0;
            sum=(sum+rt[i])/len(rt);
        com=[];
        cmt=ascii(input("comment:: "));
        com.append(cmt)
        for i in range(0,len(com)):
            print(username);
            print(com[i]);
            con=int(input("press 1 to continue browsing"));
            if(con==1):
                browse()            

def sarnee():
    print("**** SARILLERU NEEKYEVVARU ****");
    print("theatre:: navarang theatre \n show-time:: 11:30am");
    print("review: XXXX")
    se=int(input("1.book ticket \n 2.rate and comment:: "));
    if(se==1):
        print("BOOKING TICKETS!!!")
        global seats;
        seats=int(input("enter the number of seats to be booked:: "));
        global totalSeats;
        totalSeats=[];
        for i in range(0,seats):
            num=int(input("enter the seat numbers::"));
            totalSeats.append(num);
        global amount;
        amount=seats*200;
        print("total amount to be paid:: ",seats*200);
        payop=int(input("payment options:\n1.UPI payment \n2.card:: "));
        if(payop==1):
            upi=ascii(input("enter UPI pin:: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: navarang theatre \n show-time:: 11:30am");
                print("means of payment:: UPI payment");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()
        elif(payop==2):
            print("ADD CARD(all types of cards are accepted)");
            bana=ascii(input("Full name: "));
            carno=ascii(input("card number: "));
            expmon=ascii(input("expiry month: "));
            expdate=ascii(input("expiry date: "));
            cvv=ascii(input("cvv code: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: navarang theatre \n show-time:: 11:30am");
                print("means of payment:: card");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()                 
    else:
        rate=int(input("rate out of 10:: "));
        rt=[];
        rt.append(rate)
        for i in range(0,len(rt)):
            sum=0;
            sum=(sum+rt[i])/len(rt);
        com=[];
        cmt=ascii(input("comment:: "));
        com.append(cmt)
        for i in range(0,len(com)):
            print(username);
            print(com[i]);
            con=int(input("press 1 to continue browsing"));
            if(con==1):
                browse()            
    
def maharshi():
    print("**** MAHARSHI ****");
    print("theatre:: govardan theatre \n show-time:: 10:00am");
    print("review: XXXX")
    se=int(input("1.book ticket \n 2.rate and comment:: "));
    if(se==1):
        print("BOOKING TICKETS!!!")
        global seats;
        seats=int(input("enter the number of seats to be booked:: "));
        global totalSeats;
        totalSeats=[];
        for i in range(0,seats):
            num=int(input("enter the seat numbers::"));
            totalSeats.append(num);
        global amount;
        amount=seats*185;
        print("total amount to be paid:: ",seats*185);
        payop=int(input("payment options:\n1.UPI payment \n2.card:: "));
        if(payop==1):
            upi=ascii(input("enter UPI pin:: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: govardan theatre \n show-time:: 10:00am");
                print("means of payment:: UPI payment");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()
        elif(payop==2):
            print("ADD CARD(all types of cards are accepted)");
            bana=ascii(input("Full name: "));
            carno=ascii(input("card number: "));
            expmon=ascii(input("expiry month: "));
            expdate=ascii(input("expiry date: "));
            cvv=ascii(input("cvv code: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: govardan theatre \n show-time:: 10:00am");
                print("means of payment:: card");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()                 
    else:
        rate=int(input("rate out of 10:: "));
        rt=[];
        rt.append(rate)
        for i in range(0,len(rt)):
            sum=0;
            sum=(sum+rt[i])/len(rt);
        com=[];
        cmt=ascii(input("comment:: "));
        com.append(cmt)
        for i in range(0,len(com)):
            print(username);
            print(com[i]);
            con=int(input("press 1 to continue browsing"));
            if(con==1):
                browse()            

def decom():
    print("**** DEAR COMARADE ****");
    print("theatre:: rockline cinemas \n show-time:: 4:30pm");
    print("review: XXXX")
    se=int(input("1.book ticket \n 2.rate and comment:: "));
    if(se==1):
        print("BOOKING TICKETS!!!")
        global seats;
        seats=int(input("enter the number of seats to be booked:: "));
        global totalSeats;
        totalSeats=[];
        for i in range(0,seats):
            num=int(input("enter the seat numbers::"));
            totalSeats.append(num);
        global amount;
        amount=seats*150;
        print("total amount to be paid:: ",seats*150);
        payop=int(input("payment options:\n1.UPI payment \n2.card:: "));
        if(payop==1):
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                upi=ascii(input("enter UPI pin:: "));
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: rockline cinemas \n show-time:: 4:30pm");
                print("means of payment:: UPI payment");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()
        elif(payop==2):
            print("ADD CARD(all types of cards are accepted)");
            bana=ascii(input("Full name: "));
            carno=ascii(input("card number: "));
            expmon=ascii(input("expiry month: "));
            expdate=ascii(input("expiry date: "));
            cvv=ascii(input("cvv code: "));
            pay=int(input("press 1 to payment:: "));
            if(pay==1):
                print("***payment successful*** ");
                print("\nTICKET SUMMARY");
                print("theatre:: rockline cinemas \n show-time:: 4:30pm");
                print("means of payment:: card");
                ticketsum()
            else:
                print("***payment unsuccessful***");            
                browse()                 
    else:
        rate=int(input("rate out of 10:: "));
        rt=[];
        rt.append(rate)
        for i in range(0,len(rt)):
            sum=0;
            sum=(sum+rt[i])/len(rt);
        com=[];
        cmt=ascii(input("comment:: "));
        com.append(cmt)
        for i in range(0,len(com)):
            print(username);
            print(com[i]);
            con=int(input("press 1 to continue browsing"));
            if(con==1):
                browse()            

        
def conti():
    print("#########################################");
    hindi=["angrezi medium","kalank","zindagi na milegi dobaara"];
    kannada=["dia","love mocktail","odeya"];
    telugu=["sarilleru neekyavvaru","maharshi","dear commorade"];
    mov=["kannada","hindi","telugu"];
    print(".......WELCOME TO ONLINE TICKET BOOKING....... ");
    print("available movies in banglore!!");
    movies=hindi+kannada+telugu;
    tot=len(kannada)+len(hindi)+len(telugu);
    for i in range(0,tot):
        print(i+1,".",movies[i]);
    print(tot+1,"##OR## add filters");
    print(tot+2,"customer care :)");
    
        
    
def knh():
    mix1=kannada+hindi;
    print("results:: ");    
    for i in range(0,len(mix1)):
        print(i+1,".",mix1[i]);
    choice=int(input("enter your choice::"));
    if(choice==1):
        dia()
    elif(choice==2):
        lovmoc()
    elif(choice==3):
        odeya()
    elif(choice==4):
        angrez()
    elif(choice==5):
        kalank()
    elif(choice==6):
        zindagi()

def knt():
    mix2=kannada+telugu;
    print("results:: ");    
    for i in range(0,len(mix2)):
        print(i+1,".",mix2[i]);
    choice=int(input("enter your choice::"));
    if(choice==1):
        dia()
    elif(choice==2):
        lovmoc()
    elif(choice==3):
        odeya()
    elif(choice==4):
        sarnee()
    elif(choice==5):
        maharshi()
    elif(choice==6):
        decom()
    
def tnh():
    mix3=telugu+hindi;
    print("results:: ");    
    for i in range(0,len(mix3)):
        print(i+1,".",mix3[i]);    
    if(choice==4):
        sarnee()
    elif(choice==5):
        maharshi()
    elif(choice==6):
        decom()
    elif(choice==4):
        angrez()
    elif(choice==5):
        kalank()
    elif(choice==6):
        zindagi()    

def ticketsum():
    print("number of seats:: ",seats);
    print("seat numbers:: ",totalSeats);
    print("amount paid:: ",amount);
    
    con=int(input("press 1 to continue browsing \n press 2 to logout"));
    if(con==1):
        browse()
    elif(con==2):
        exit(0)
    
    

browse()
browse()
conti()
signUp()
orcase()
login()
options()
kalank()
filters()
angrez()
dia()
lovmoc()
zindagi()
odeya()
sarnee()
maharshi()
decom()
knh()
knt()
tnh()
ticketsum()