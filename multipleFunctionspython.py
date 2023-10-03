class multipleFunctionspython():
    def Subfields():
        List=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Subfields in AI are:")
        for subfield in List:
            print(subfield)
    def oddEven():    
        num=int(input("Enter the number:"))
        if ((num%2)==1):
            print(num,"is Odd number")
            msg="Odd number"
        else:
            print(num,"is Even number")
            msg="Even number"
        return msg
    def Eligible():
        Gender= str(input("Your Gender: "))
        Age=int(input ("Your Age:"))
        if((Gender== "Male") and (Age>=21)):
            print("ELIGIBLE")
        elif((Gender=="Female") and (Age>=18)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def percentage():
        Subjects=["Subject1","Subject2","Subject3","Subject4","Subject5"]
        Subject1=int(input("Subject1:"))
        Subject2=int(input("Subject2:"))
        Subject3=int(input("Subject3:"))
        Subject4=int(input("Subject4:"))
        Subject5=int(input("Subject5:"))
        total=Subject1+Subject2+Subject3+Subject4+Subject5
        percentage=(total/500.0)*100
        print("Total",total)
        print("Percentage:", percentage)
    def triangle():
        Height=float(input("Height:"))
        Breadth=float(input("Breadth:"))
        Area=0.5*Breadth*Height
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", Area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        perimeter= Height1+Height2+Breadth
        print("Perimeter Formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", perimeter)