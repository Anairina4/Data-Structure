#Exercitiu 1
my_list = [7,8,9,2,3,1,4,10,5,6]
print("lista mea este = ", my_list, type(my_list))

#Exercitiu 2
ascendent_list = my_list.copy()
ascendent_list.sort()
print("Lista sortata ascendent este: ", ascendent_list)
print("my list este: ", my_list)

#Exercitiu 3
descendent_list = ascendent_list.copy()
descendent_list.reverse()
print("Lista sortata descendent este:", descendent_list)
print("Lista sortata ascendent este: ", ascendent_list)
print("my list este: ", my_list)

#Exercitiu 4
my_Sliced_list = ascendent_list[1::2]
print(my_Sliced_list)

#Exercitiu 5
my_Sliced_list = ascendent_list[0::2]
print(my_Sliced_list)

#Exercitiu 6
my_Sliced_list = ascendent_list[2::3]
print(my_Sliced_list)