import mysql.connector
import random
import numpy as np
import pandas as pd
import datetime
from tabulate import tabulate
import time
from tqdm import tqdm

def tr():
    dt=datetime.datetime.now().replace(microsecond=0)
    print()
    print("                                                              Y/M/D     H:M:S")
    print("                                                           ",dt)

def menu():
    tr()
    print()
    print()
    print("----------------------THE BANK----------------------")
    print("              What Do You Want To Do??              ")
    print()
    print("  1 = Create a new Account")
    print("  2 = Login to an existing Account")
    print("  3 = Only For Manager And Trusted Staff")
    print("----------------------------------------------------")
    print()
    print()

def menu2():
    tr()
    print()
    print()
    print("---------------WELCOME  TO  THE  BANK---------------")
    print("                How Can I Help You??                ")
    print()
    print("  1  = Withdraw Money")
    print("  2  = Deposit Money")
    print("  3  = Pay Money To Another Person")
    print("  4  = Donate Money To Help People")
    print("  5  = Check Out Other Facilities-")
    print("       • Buy Debit Card")
    print("       • Buy Credit Card")
    print("       • Exchange Foriegn Currency")
    print("       • Loan")
    print("  6  = Show Details")
    print("  7  = Edit Details")
    print("  8  = View Transaction History")
    print("  9  = Delete Account")
    print("  10 = LOGOUT")
    print("----------------------------------------------------")
    print()
    print()

def wm():
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    acc=input("\nEnter Your Account no.- ")
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        amt=float(input("Enter Amount To Be Withdrawn- ₹")) 
        i="select Balance from accounts where Acc_no=%s"
        o=[(acc)]
        mycursor.execute(i,o)
        for x in mycursor:
            if x[0]-amt>=0:
                i="update accounts set Balance = Balance-%s where Acc_no=%s"
                o=[(amt,acc)]
                mycursor.executemany(i,o)
                mydb.commit()
                print()
                print("Amount Withdrawn")
                dt=datetime.datetime.now().replace(microsecond=0)
                i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
                o=[(amt,"Withdrawn Money",dt)]
                mycursor.executemany(i,o)
                mydb.commit()
                i="select Balance from accounts where Acc_no=%s"
                o=[(acc)]
                mycursor.execute(i,o)
                for x in mycursor:
                    print("YOUR CURRENT BALANCE IS ₹", x)
            else:
                print("You Don't Have Enough Money")

def dm():
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    acc=input("\nEnter Your Account no.- ")
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        amt=float(input("Enter Amount That You Want To Deposit- ₹"))
        i="update accounts set Balance = Balance+%s where Acc_no=%s"
        o=[(amt,acc)]
        mycursor.executemany(i,o)
        mydb.commit()
        print()
        print("Amount Deposited")
        dt=datetime.datetime.now().replace(microsecond=0)
        i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
        o=[(amt,"Deposited Money",dt)]
        mycursor.executemany(i,o)
        mydb.commit()
        i="select Balance from accounts where Acc_no=%s"
        o=[(acc)]
        mycursor.execute(i,o)
        for x in mycursor:
            print("YOUR CURRENT BALANCE IS ₹", x)

def pm():
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    acc=input("\nEnter Your Account no.- ")
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        acc1=int(input("Enter Account no. Of The Creditor- "))
        i="select * from accounts where Acc_no = {}".format(acc1)
        mycursor.execute(i)
        q=mycursor.fetchall()
        if q==[]:
            print("\n\nAccount Not Found")
        else:
            amt=float(input("Enter Amount That You Want To Pay- ₹"))
            i="update accounts set Balance = Balance+%s where Acc_no=%s"
            o=[(amt,acc1)]
            mycursor.executemany(i,o)
            mydb.commit()            
            i="update accounts set Balance = Balance-%s where Acc_no=%s"
            o=[(amt,acc)]
            mycursor.executemany(i,o)
            mydb.commit()
            print()
            print("Amount Payed")
            dt=datetime.datetime.now().replace(microsecond=0)
            i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
            o=[(amt,"Money Payed To Another Person",dt)]
            mycursor.executemany(i,o)
            mydb.commit()
            i="select Balance from accounts where Acc_no=%s"
            o=[(acc)]
            mycursor.execute(i,o)
            for x in mycursor:
                print("YOUR CURRENT BALANCE IS ₹", x)

def donate():
    acc=input("\nEnter Your Account no.- ₹")
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        amt=float(input("Enter Amount That You Want To Donate- "))
        i="select Balance from accounts where Acc_no=%s"
        o=[(acc)]
        mycursor.execute(i,o)
        for x in mycursor:
            if x[0]-amt>=0:
                i="update accounts set Balance = Balance-%s where Acc_no=%s"
                o=[(amt,acc)]
                mycursor.executemany(i,o)
                mydb.commit()
                print()
                            
                r=random.randint(1,7)
                if r==1:
                    print("Dear Donator, Thank You for your great generosity!")
                    print("We at KATHA really appreciate your donation of ₹.",amt)
                elif r==2:
                    print("Thank You for donating ₹",amt," rupees to our Organisation")
                elif r==3:
                    print("We at Goonj really appreciate your donation of ₹",amt," THANK YOU")
                elif r==4:
                    print("Thank You for your generous gift of ₹",amt," to WHO!")
                    print("We are thrilled to have your support")
                elif r==5:
                    print("Your support of ₹",amt," is invaluable to us")
                    print("Thanks A Lot from UNICEF")
                elif r==6:
                    print("Together we are making a difference.")
                    print("Your support of ₹",amt," for our mission is deeply gratifying to us!")
                    print("                                        - CRY Organisation")

                dt=datetime.datetime.now().replace(microsecond=0)
                i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
                o=[(amt,"Donated Money",dt)]
                mycursor.executemany(i,o)
                mydb.commit()

                i="select Balance from accounts where Acc_no=%s"
                o=[(acc)]
                mycursor.execute(i,o)
                for x in mycursor:
                    print()
                    print()
                    print("YOUR CURRENT BALANCE IS ₹", x)

            else:
                print("You Don't Have Enough Money")

def dc():
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    acc=input("\nEnter Your Account no.- ")
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        i="select Debit_Card from accounts where Acc_no=%s"
        o=[(acc)]
        mycursor.execute(i,o)
        for y in mycursor:
            if y[0]=="NO":
                i="update accounts set Debit_Card = %s where Acc_no=%s"
                o=[("YES",acc)]
                mycursor.executemany(i,o)
                mydb.commit()
                print()
                print("Debit Card Purchased")
                print("Further Information will be sent to you via your Email")
                dt=datetime.datetime.now().replace(microsecond=0)
                i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
                o=[(0,"Purchased Debit Card",dt)]
                mycursor.executemany(i,o)
                mydb.commit()
            else:
                print("You Already Have A Debit Card")

def cc():
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    acc=input("\nEnter Your Account no.- ")
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        i="select Credit_Card from accounts where Acc_no=%s"
        o=[(acc)]
        mycursor.execute(i,o)
        for y in mycursor:
            if y[0]=="NO":
                i="update accounts set Credit_Card = %s where Acc_no=%s"
                o=[("YES",acc)]
                mycursor.executemany(i,o)
                mydb.commit()
                print()
                print("Credit Card Purchased")
                print("Further Information will be sent to you via your Email")
                dt=datetime.datetime.now().replace(microsecond=0)
                i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
                o=[(0,"Purchased Credit Card",dt)]
                mycursor.executemany(i,o)
                mydb.commit()
            else:
                print("You Already Have A Credit Card")

def fc():
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    print("We Currently Take The Following Currency-")
    print("1 = US Dollar             ($)")
    print("2 = Euro                  (€)")
    print("3 = Japanese Yen          (¥)")
    print()
    print("Rate Of Interest = 5%")
    print("Your Money Will Be Deposited Into Your Account")
    print()

    acc=input("\nEnter Your Account no.- ")
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        print()
        ch3=int(input("Enter what you want to exchange- "))
        if ch3==1:
            print()
            amt=float(input("Enter Amount Of Money You Want To Exchange- $"))
            amt=(amt*73.98)-((5/100)*amt)
            print("Money Converted Into Rupees with 5% interest = ₹",amt)
            i="update accounts set Balance = Balance+%s where Acc_no=%s"
            o=[(amt,acc)]
            mycursor.executemany(i,o)
            mydb.commit()
            print()
            print("Amount Deposited in your account")
            dt=datetime.datetime.now().replace(microsecond=0)
            i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
            o=[(amt,"Exchanged US Dollars",dt)]
            mycursor.executemany(i,o)
            mydb.commit()
            i="select Balance from accounts where Acc_no=%s"
            o=[(acc)]
            mycursor.execute(i,o)
            for x in mycursor:
                print("YOUR CURRENT BALANCE IS ₹", x)
        elif ch3==2:
            print()
            amt=float(input("Enter Amount Of Money You Want To Exchange- €"))
            amt=(amt*87.85)-((5/100)*amt)
            print("Money Converted Into Rupees with 5% interest = ₹",amt)
            i="update accounts set Balance = Balance+%s where Acc_no=%s"
            o=[(amt,acc)]
            mycursor.executemany(i,o)
            mydb.commit()
            print()
            print("Amount Deposited in your account")
            dt=datetime.datetime.now().replace(microsecond=0)
            i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
            o=[(amt,"Exchanged Euros",dt)]
            mycursor.executemany(i,o)
            mydb.commit()
            i="select Balance from accounts where Acc_no=%s"
            o=[(acc)]
            mycursor.execute(i,o)
            for x in mycursor:
                print("YOUR CURRENT BALANCE IS ₹", x)
        elif ch3==3:
            print()
            amt=float(input("Enter Amount Of Money You Want To Exchange- ¥"))
            amt=(amt*0.72)-((5/100)*amt)
            print("Money Converted Into Rupees with 5% interest = ₹")
            i="update accounts set Balance = Balance+%s where Acc_no=%s"
            o=[(amt,acc)]
            mycursor.executemany(i,o)
            mydb.commit()
            print()
            print("Amount Deposited in your account")
            dt=datetime.datetime.now().replace(microsecond=0)
            i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
            o=[(amt,"Exchanged Japanese Yen",dt)]
            mycursor.executemany(i,o)
            mydb.commit()
            i="select Balance from accounts where Acc_no=%s"
            o=[(acc)]
            mycursor.execute(i,o)
            for x in mycursor:
                print("YOUR CURRENT BALANCE IS ₹", x)
        else:
            print("Enter a valid no.")

def ll():
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    print() 
    print("What kind of Loan do u need?")
    print("1 = Home Loan")
    print("2 = Personal Loan")
    print("3 = Business Loan")
    print("4 = Gold Loan")
    print()
    ll1=int(input("Enter your choice- "))
    acc=int(input("Enter Your Account no.- "))
    if ll1==1:
        print()
        print("Max Loan = ₹5 crore")
        print("Rate Of Interest per annum= 6%")
        print()
        print("Upload Passport Size Photgraph                                     |  CURRENTLY UNAVAILABLE  |  ")
        print("Upload Adress Proof                                                |  PLEASE TRY AGAIN LATER |  ")
        print("Upload Age Proof (must be between 20-70)                           |  OR SUBMIT THEM TO YOUR |  ")
        print("Upload PAN Card / Driving Licence / Passport / Voter ID            |      NEAREST BRANCH     |  ")
        print()
        bl=int(input("Enter Amount for Loan (in figures)- "))
        tl=int(input("Enter Time for Loan (in years)- "))
        print()
        amt=bl*(1+(tl*6))
        print("You Have to Deposit ₹",amt)
        an=random.randint(10000000000,9999999999)
        print("Your Application number is ",an)

        i="update accounts set Loan = %s where Acc_no=%s"
        o=[(amt,acc)]
        mycursor.executemany(i,o)
        mydb.commit()

        dt=datetime.datetime.now().replace(microsecond=0)
        i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
        o=[(amt,"Took Home Loan",dt)]
        mycursor.executemany(i,o)
        mydb.commit()

    elif ll1==2:
        print()
        print("Max Loan = ₹25 crore")
        print("Rate Of Interest per annum= 12%")
        print()
        print("Upload Passport Size Photgraph                                     |  CURRENTLY UNAVAILABLE  |  ")
        print("Upload Adress Proof                                                |  PLEASE TRY AGAIN LATER |  ")
        print("Upload Age Proof (must be between 20-70)                           |  OR SUBMIT THEM TO YOUR |  ")
        print("Upload PAN Card / Driving Licence / Passport / Voter ID            |      NEAREST BRANCH     |  ")
        print()
        bl=int(input("Enter Amount for Loan (in figures)- ₹"))
        tl=int(input("Enter Time for Loan (in years)- "))
        print()
        amt=bl*(1+(tl*12))
        print("You Have to Deposit ₹",amt)
        an=random.randint(10000000000,9999999999)
        print("Your Application number is ",an)

        i="update accounts set Loan = %s where Acc_no=%s"
        o=[(amt,acc)]
        mycursor.executemany(i,o)
        mydb.commit()

        dt=datetime.datetime.now().replace(microsecond=0)
        i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
        o=[(amt,"Took Personal Loan",dt)]
        mycursor.executemany(i,o)
        mydb.commit()

    elif ll1==3:
        print()
        print("Max Loan = ₹100 crore")
        print("Rate Of Interest per annum= 15%")
        print()
        print("Upload Passport Size Photgraph                                     |  CURRENTLY UNAVAILABLE  |  ")
        print("Upload Adress Proof                                                |  PLEASE TRY AGAIN LATER |  ")
        print("Upload Age Proof (must be between 20-70)                           |  OR SUBMIT THEM TO YOUR |  ")
        print("Upload PAN Card / Driving Licence / Passport / Voter ID            |      NEAREST BRANCH     |  ")
        print()
        bl=int(input("Enter Amount for Loan (in figures)- ₹"))
        tl=int(input("Enter Time for Loan (in years)- "))
        print()
        amt=bl*(1+(tl*15))
        print("You Have to Deposit ₹",amt)
        an=random.randint(10000000000,9999999999)
        print("Your Application number is ",an)

        i="update accounts set Loan = %s where Acc_no=%s"
        o=[(amt,acc)]
        mycursor.executemany(i,o)
        mydb.commit()

        dt=datetime.datetime.now().replace(microsecond=0)
        i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
        o=[(amt,"Took Business Loan",dt)]
        mycursor.executemany(i,o)
        mydb.commit()

    elif ll1==4:
        print()
        print("Max Loan = ₹10 crore")
        print("Rate Of Interest per annum= 8%")
        print()
        print("Upload Passport Size Photgraph                                     |  CURRENTLY UNAVAILABLE  |  ")
        print("Upload Adress Proof                                                |  PLEASE TRY AGAIN LATER |  ")
        print("Upload Age Proof (must be between 20-70)                           |  OR SUBMIT THEM TO YOUR |  ")
        print("Upload PAN Card / Driving Licence / Passport / Voter ID            |      NEAREST BRANCH     |  ")
        print()
        bl=int(input("Enter Amount for Loan (in figures)- ₹"))
        tl=int(input("Enter Time for Loan (in years)- "))
        print()
        amt=bl*(1+(tl*8))
        print("You Have to Deposit ₹",amt)
        an=random.randint(10000000000,9999999999)
        print("Your Application number is ",an)

        i="update accounts set Loan = %s where Acc_no=%s"
        o=[(amt,acc)]
        mycursor.executemany(i,o)
        mydb.commit()

        dt=datetime.datetime.now().replace(microsecond=0)
        i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
        o=[(amt,"Took Gold Loan",dt)]
        mycursor.executemany(i,o)
        mydb.commit()
    else:
        print("Enter Valid Choice")


def buy():
    print()
    print()
    print("Other Facilities- ")
    print("1 = Buy Debit Card")
    print("2 = Buy Credit Card")
    print("3 = Exchange Foriegn Currency")
    print("4 = Loan")
    print()
    print("More Facilities Coming Soon......")
    print()
    ch2=int(input("Enter your choice- "))
    if ch2==1:
        print()
        dc()
    elif ch2==2:
        print()
        cc()
    elif ch2==3:
        print()
        fc()
    elif ch2==4:
        print()
        ll()
    else:
        print()
        print()
        print("Enter a valid no.")

def sd():
    acc=input("\nEnter Your Account no.- ")
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        i="select Name , Adress , Ph_no , Balance , Debit_Card , Credit_Card , Email_ID from accounts where Acc_no=%s"
        o=[(acc)]
        mycursor.execute(i,o)
        for x in mycursor:
            print()
            print("Name- ", x[0])
            print("Adress- ", x[1])
            print("Phone no.- ", x[2])
            print("Balance- ", x[3])
            print("Debit_Card- ", x[4])
            print("Credit_Card- ", x[5])
            print("Email_id- ", x[6])

def ed():
    acc=input("\nEnter Your Account no.- ")
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        print("1 = Change Name")
        print("2 = Change Adress")
        print("3 = Change Phone no.")
        print("4 = Change Password")
        a2=int(input("Enter No. According To What You Want To Change- "))
        if a2==1:
            z=input("Enter New Name- ")
            z1=input("Confirm Your Name-")
            if z==z1:
                i="update accounts set Name = %s where Acc_no = %s"
                o=[(z,acc)]
                mycursor.executemany(i,o)
                mydb.commit()
                print()
                print("Change Saved")
                dt=datetime.datetime.now().replace(microsecond=0)
                i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
                o=[(0,"Name Changed",dt)]
                mycursor.executemany(i,o)
                mydb.commit()
            else:
                print("Incorrect Name")
                print("Try Again")
        elif a2==2:
            z=input("Enter New Adress- ")
            z1=input("Confirm Your Adress-")
            if z==z1:
                i="update accounts set Adress = %s where Acc_no = %s"
                o=[(z,acc)]
                mycursor.executemany(i,o)
                mydb.commit()
                print()
                print("Change Saved")
                dt=datetime.datetime.now().replace(microsecond=0)
                i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
                o=[(0,"Adress Changed",dt)]
                mycursor.executemany(i,o)
                mydb.commit()
            else:
                print("Incorrect Adress")
                print("Try Again")
        elif a2==3:
            z=input("Enter New Phone no.- ")
            z1=input("Confirm Your Phone no.-")
            if z==z1:
                i="update accounts set Ph_no = %s where Acc_no = %s"
                o=[(z,acc)]
                mycursor.executemany(i,o)
                mydb.commit()
                print()
                print("Change Saved")
                dt=datetime.datetime.now().replace(microsecond=0)
                i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
                o=[(0,"Phone no. Changed",dt)]
                mycursor.executemany(i,o)
                mydb.commit()
            else:
                print("Incorrect Phone no.")
                print("Try Again")
        elif a2==4:
            z=input("Enter New Password- ")
            z1=input("Confirm Your Phone no.-")
            if z==z1:
                i="update accounts set Password = %s where Acc_no = %s"
                o=[(z,acc)]
                mycursor.executemany(i,o)
                mydb.commit()
                print()
                print("Change Saved")
                dt=datetime.datetime.now().replace(microsecond=0)
                i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
                o=[(0,"Password Changed",dt)]
                mycursor.executemany(i,o)
                mydb.commit()
            else:
                print("Incorrect Password")
                print("Try Again")
        elif a2==5:
            z=input("Enter New Email ID- ")
            z1=input("Confirm Your Phone no.-")
            if z==z1:
                i="update accounts set Email_ID = %s where Acc_no = %s"
                o=[(z,acc)]
                mycursor.executemany(i,o)
                mydb.commit()
                print()
                print("Change Saved")
                dt=datetime.datetime.now().replace(microsecond=0)
                i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
                o=[(0,"Email ID Changed",dt)]
                mycursor.executemany(i,o)
                mydb.commit()
            else:
                print("Incorrect Email ID")
                print("Try Again")
        else:
            print("Enter Valid no.")
    
def st():
    acc=input("\nEnter Your Account no.- ")
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        i="select * from a{}".format(acc)
        mycursor.execute(i)
        gg=mycursor.fetchall()
        gg1="Amount","                History                ","Date & Time (Years/Months/Day Hr:Min:Sec)"
        print(tabulate(gg,headers=gg1,tablefmt="github"))
        

def dd():
    acc=input("\nEnter Your Account no.- ")
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        i="drop table a{}".format(acc)
        mycursor.execute(i)
        i="delete from accounts where Acc_no = %s"
        o=[(acc)]
        mycursor.execute(i,o)
        mydb.commit()
        print()
        print("Account Deleted")

def logout():
    print()
    print("LOGGED OUT SUCCESSFULLY")
    print("You Can Now Safely Close The Program!")

def register():
    print()
    n=input("\nEnter Your Name- ")
    d=input("\nEnter Your Adress- ")
    e=input("\nEnter Your Email_ID- ")
    c=int(input("\nEnter Your Phone No.- "))
    m1=datetime.date.today()
    m=m1.month
    if len(str(c))==10:
        mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
        mycursor=mydb.cursor()
        p=input("\nEnter Your Password (8 CHARACTERS MAX)- ")
        acc=random.randint(10000,100000)
        i="select * from accounts where Acc_no = {}".format(acc)
        mycursor.execute(i)
        q=mycursor.fetchall()
        if q==[]:
            print()
            print()
            i="insert into accounts (Name,Acc_no,Adress,ph_no,Password,Balance,Debit_Card,Credit_Card,Email_ID,Month,Loan) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            o=[(n,acc,d,c,p,0,"NO","NO",e,m,0)]
            mycursor.executemany(i,o)
            mydb.commit()
            for i in tqdm(range(0,100), total = 100, 
                desc ="CREATING ACCOUNT "): 
                time.sleep(.1)
            print("ACCOUNT CREATED")
            print()
            print(acc,"is your account no.")
            print(p,"is your password")
            print("REMEMBER THEM!!!")
            print()
            print()
            i="create table a{} (Amount float , History varchar(50) , Date_and_Time varchar(100))".format(acc)
            mycursor.execute(i)
            mydb.commit()
            dt=datetime.datetime.now().replace(microsecond=0)
            i="insert into a{} (Amount,History,Date_and_Time) values (%s,%s,%s)".format(acc)
            o=[(0,"Account Created",dt)]
            mycursor.executemany(i,o)
            mydb.commit()
        else:
            print()
            print()
            print("Sorry for inconvinience")
            print("Please Try Again")
    else:
        print("INVALID PHONE NO.")

def login():
    mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
    mycursor=mydb.cursor()
    acc=input("\nEnter Your Account no.- ")
    i="select * from accounts where Acc_no = {}".format(acc)
    mycursor.execute(i)
    q=mycursor.fetchall()
    if q==[]:
        print("\n\nAccount Not Found")
    else:
        p=input("\nEnter Password- ")
        print()
        print()
        for i in tqdm(range(0,100), total = 100, 
            desc ="Logging In To Your Account"): 
            time.sleep(.1)
        i="select Password from accounts where Acc_no=%s"
        o=[(acc)]
        mycursor.execute(i,o)
        for y in mycursor:
            if y[0]==p:
                print()
                print()
                print("You are now Logged In")
                print()
                print()
                while True:
                    menu2()
                    ch1=int(input("Enter Choice- "))
                    if ch1==1:
                        wm()
                        print()
                        print()
                        ch1=int(input("Press 0 to continue and any other no. to stop- "))
                        if ch1!=0:
                            break
                    elif ch1==2:
                        dm()
                        print()
                        print()
                        ch1=int(input("Press 0 to continue and any other no. to stop- "))
                        if ch1!=0:
                            break
                    elif ch1==3:
                        pm()
                        print()
                        print()
                        ch1=int(input("Press 0 to continue and any other no. to stop- "))
                        if ch1!=0:
                            break
                    elif ch1==4:
                        donate()
                        print()
                        print()
                        ch1=int(input("Press 0 to continue and any other no. to stop- "))
                        if ch1!=0:
                            break
                    elif ch1==5:
                        buy()
                        print()
                        print()
                        ch1=int(input("Press 0 to continue and any other no. to stop- "))
                        if ch1!=0:
                            break
                    elif ch1==6:
                        sd()
                        print()
                        print()
                        ch1=int(input("Press 0 to continue and any other no. to stop- "))
                        if ch1!=0:
                            break
                    elif ch1==7:
                        ed()
                        print()
                        print()
                        ch1=int(input("Press 0 to continue and any other no. to stop- "))
                        if ch1!=0:
                            break
                    elif ch1==8:
                        st()
                        print()
                        print()
                        ch1=int(input("Press 0 to continue and any other no. to stop- "))
                        if ch1!=0:
                            break
                    elif ch1==9:
                        dd()
                        ch1=1
                        if ch1!=0:
                            break
                    elif ch1==10:
                        logout()
                        ch1=1
                        if ch1!=0:
                            break
                    else:
                        print("\n\nEnter valid no.")

            else:
                print("\nIncorrect Password")
                login()

def secret():
    w=int(input("Enter The Secret Code- "))
    print()
    if w==12345:
        print("PASSCODE CORRECT")
        print()
        print()
        mydb=mysql.connector.connect(host='localhost',user='root',password='WhyDoITellU',database='Bank',auth_plugin='caching_sha2_password')
        mycursor=mydb.cursor()
        i="select * from accounts"
        mycursor.execute(i)
        gg=mycursor.fetchall()
        gg1="S.no.","Account no.","Name","Adress","Password","Balance","Phone no.","Debit Card","Credit Card","Email ID","Loan"
        print(tabulate(gg,headers=gg1,showindex="always",tablefmt="github"))
    else:
        print("PASSCODE  INCORRECT")

while True:
    menu()
    ch=int(input("Enter Choice- "))
    if ch==1:
        register()
        ch=int(input("\n\nPress 0 for Home and any other no. to stop- "))
        if ch!=0:
            break
    elif ch==2:
        login()
        ch=int(input("\n\nPress 0 for Home and any other no. to stop- "))
        if ch!=0:
            break
    elif ch==3:
        secret()
        ch=int(input("\n\nPress 0 for Home and any other no. to stop- "))
        if ch!=0:
            break
    else:
        print("\n\nEnter valid no.")    
