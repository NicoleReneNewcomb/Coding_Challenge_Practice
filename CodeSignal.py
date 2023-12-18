def main():
    attributes = ['make', 'model', 'year','color','condition', 'mileage']
    myCar1 = ["Ford", "F150", 2019]
    myCar5 = ["BMW", "M3", 2020, "Blue", "Good", 58674]

    # myInt = 3
    # myFloat = 3.455
    # print(45.45.hex())

    # myDict = {1: ["Rain"], 2: "Clouds", 3: "Sun"}
    # myDict[1].append("fog")
    # del myDict[2]
    # print(myDict)

    myDict = {"majid":"hot", "nicole":"not"}
    myDict.update({"bob":"cold", 'nicole':'super hot'})
    myDict['carly'] = "sad"
    myDict.clear()
    print(myDict)

    # print(myList)
    # myList[:3] = [1,2,3]
    # print(myList)

    # x = 1, 2, 3
    # print(x)

    # myList3 = [x * 3 for x in range(6)]
    # myList4 = myList3
    # myList3.pop()
    # myList3.pop()
    # print(myList3)
    # print(myList4)

    # my1 = True
    # my2 = my1
    # print(id(my1))
    # print(id(my2))

def changeList(myList):
    myList.insert(0, 22)
    myList.insert(0, 98)
    print(myList)
    return


    # print(myList)
    # del myList[3]
    # print(myList[::-1])
    # myList.extend([1, 3, 4])
    # print(myList)

    # print("Hello"[::-1])

    # genre = "transcendental"
    # print(genre[:-8])
    # print(genre[-7:9])

    # my_num = -5 % 4
    # print(my_num)

    # myDict = dict(zip(attributes, myCar5))
    # print(myDict)

    # for val in enumerate(attributes):
    #     print(val)

    # myCar5Dict = dict(zip(attributes,myCar5))
    # car5Obj = car(**myCar5Dict)
    # print(car5Obj, car5Obj.condition, car5Obj.mileage)

    # input = "Four score and seven years ago"
    # print(input.slice(-3))
    # print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])

    # myCar1 = car(make="Ford", model="F150", year=2019)
    # myCar2 = car(make="Kia", model="Sportage", year=2005, color="Red")
    # myCar3 = car(make="Tesla", model="M3", year=1345, color="Blue", condition="Good")
    # myCar4 = car(make="BMW", model="M3", year=2020, color="Blue", condition="Good", mileage=76500)
    # myCar5 = car(**{'make':"Hornet", 'model':"Goldilocks", 'year':2023, 'color':"Purple", 'condition':"Excellent", 'mileage':12350})

    # carList = [myCar1,myCar2,myCar3,myCar4,myCar5]

    # for theCar in carList:
    #     for value in theCar.__dict__.values():
    #         print(value, end=' ')
    #     print()

    # myCar1.car_sound()
    # myCar5.car_sound()
    # print(myCar5.make)

    # myDict = {"hi": 1, "hello" : "no", "blue": False}
    # myDict["hi"] = "newone"
    # print(myDict['hi'])

class car:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def car_sound(self):
        print("Vroom, vroom...")
        print("I'm a", self.model)

    def get_make(self):
        return self.make
    
    def set_make(self, new_make):
        self.make = new_make

    def __str__(self):
        return self.make + " " + self.model + " " + str(self.year)


# class euro(car):

#     def __init__(self, make, model, year, euro):
#         super().__init__(make, model, year)
#         self.euro = euro

#     def car_sound(self):
#         print("Vroom, vroom...")
#         print("I'm a European car: ", self.model)

if __name__ == "__main__":
  main()

# import math

# x = 152.5678
# y = 55568.9999
# z = 2.00001
# print(str(x))
# print(str(y))
# print(str(z))
# print("Here are numbers:",x,y,z, sep="", end="   ")
# print("Here are numbers: %.3e" % x)
# print(f"New number {y:#.3g}")


# newString = '\n'
# rawString = r'\n\n\n'
# numberNewLines = newString*4
# print(repr(numberNewLines))
# print(rawString)
# myString = numberNewLines + 'My phrase' +r'\'s here:'
# print(myString)
# print(myString.index('ra'))

# a = True
# b = False
# print(not (a == b))
# print(a == (not b))
# print(not a == b)



# xs = [()]
# res = [False] * 2
# if xs:
#     res[0] = True
# if xs[0]:
#     res[1] = True
# print(res)