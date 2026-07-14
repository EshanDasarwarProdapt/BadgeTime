class Overloadingdemo():
    def showdetails(self,*args):
        if len(args) == 1:
            print(f"Car brand : {args[0]}")

        elif len(args) == 2:
            print(f"Car Brand : {args[0]}, Model : {args[1]}")

        elif len(args) == 3:
            print(f"Car brand : {args[0]}, model : {args[1]}, year : {args[2]}")

        else:
            print("Invalid args")

def overloading():
    demo = Overloadingdemo()
    demo.showdetails("toyota")
    demo.showdetails("Honda", "civic")
    demo.showdetails("Ford", "Mustang", 2020)
    demo.showdetails("chervrolet", "Camaro", 2021, "Extra")

