cars=['bmw','audi','toyota','subaru']
cars.sort()            #此时是默认用字母排序，且不可更改。
print(cars)

cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)#注意,这是按字母相反顺序排序，我因为将v写成s而算错           
print(cars)

cars=['bmw','audi','toyota','subaru'] 
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))   #sorted对列表的影响是有限的

cars=['bmw','audi','toyota','subaru'] 
print(sorted(cars, reverse=True))

cars=['bmw','audi','toyota','subaru']#sort()yusorted()有本质区别，不可替换。
print(cars)
cars.reverse()       
print(cars)

cars=['bmw','audi','toyota','subaru'] 
print(len(cars))