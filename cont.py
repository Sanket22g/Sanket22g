import pyttsx3
import matplotlib.pyplot as plt
engine =pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150) 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female
contact ={}
def contacts():
        engine.say("how many cantact are you want to store = ")
        engine.runAndWait()
        j=int(input("how many contact are you  want to store = "))
        for o in range(j):
             n = input("Enter the name of which you want to save = ")
             y =n.lower()
             m=int(input("Enter the Number"))
             contact.update({y:m})
        p=contact.values()
        print(f"The save contact is  {len(p)}")
        try :
             no = input("for search contact write s = ".lower())
             if no =="s":
                  h = input("serch the contact")
                  g =h.lower()
                  contact.get(g)
                  print(f"The namber is {contact.get(g)}")
        except Exception as e:
               print("no number is present in  your phone ",e)

        ra = input("are you want to delet contact yes/no = ".lower())
        if ra =="yes":
           inl=input("enter the number which you want to delet")
           contact.pop(inl)
           op=contact.values()
           print(f"The save contact is  {len(op)}")
        lo=input("are you want to see the save contact yes or no = ".lower())
        if lo =="yes":
          print(contact)
          plt.bar(contact)
          plt.show()
        
while True:
    contacts()
