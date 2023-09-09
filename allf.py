class allfun():
    def femi():
        print("My fn")
    
    def Subfields():
        print("Sub-fields in AI are:\nMachine Learning \nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing")     
    def OddEven():
        n=int(input("Enter a number:"))
        if(n%2==0):
            print(n," is Even number")
        else:
            print(n," is odd number")  
            
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(((gender=='Male') and (age>=21)) or ((gender=='Female') and (age>=18))):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    def percentage():
        s1=int(input("Subject1="))
        s2=int(input("Subject2="))
        s3=int(input("Subject3="))
        s4=int(input("Subject4="))
        s5=int(input("Subject5="))
        total=s1+s2+s3+s4+s5
        print("Total: ",total)
        print("Percentage: " ,(total/5))
        
    def triangle():
        h=int(input("Height: "))
        b=int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(h*b)/2)
        h1=int(input("Height1: "))
        h2=int(input("Height2: "))
        b1=int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",h1+h2+b1)  