print ("Dance Institute")
age=int(input("Enter you age \n"))
if age <= 6:
 print("Not eligible")
else:
   print("Type of dance")
   print("1. Classical")
   print("2. kathak")
   print("3. kuchupudi")
   print("4. Yakshagana")

   type=input()
   if type== "1":
       print("Classical dance details")
       f = open("classical.txt", "r")
       print(f.read())
       print("Fee Details : 1000")
       print("Address : Kengeri,Banglore")
       print("Contact:9876543210")
   elif type=="2":
       print("Kathak dance details")
       f = open("Kathak.txt", "r")
       print(f.read())
       print("Fee Details : 1000")
       print("Address : Kengeri,Banglore")
       print("Contact:9876543210")
   elif type=="3":
        print("kuchpudi dance details")
        f = open("Kuchupudi.txt", "r")
        print(f.read())
        print("Fee Details : 1000")
        print("Address : Kengeri,Banglore")
        print("Contact:9876543210")
   elif type=="4":
        print("yakshagana dance details")
        f = open("Yakshagana.txt", "r")
        print(f.read())
        print("Fee Details : 1000")
        print("Address : Kengeri,Banglore")
        print("Contact:9876543210")
   else:
        print("Invalid input")

 
