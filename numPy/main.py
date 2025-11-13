import numpy as np
import math
print(np.__version__) # versiyani aniqlash.

####################################
my_list = [1, 2, 3]
my_list = my_list * 2
print(my_list)

####################################
array = np.array([1, 2, 3, 4])
array = array * 5
print(array)
print(type(array)) # array turini ko'rish.

######################################
array1 = np.array("A")
array2 = np.array(["A", "B", "C"])
array3 = np.array([[["A", "B", "C"], ["D", "E", "F"]], [["G", "H", "I"], ["J", "K", "L"]]]) # bir xil bo'lishi kerak.

print(array1.ndim)# arrayni nechi o'lchovligini aniqlash.
print(array2.ndim)
print(array3.ndim)

####################################
array4 = np.array([[["A", "B", "C"], ["D", "E", "F"]],
                   [["G", "H", "I"], ["J", "K", "L"]]])
print(array4.shape) # qanday strukturada ekanligini aniqlab beradi.
print(array4[1,1,2])
word = array4[0,0,0] + array4[0,1,0]*2
print(word)

#####################################
array5 = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])
print(array5.ndim)
print(array5.shape)

print(array5[:2 , 2:]) #keraklisini bo'lib olish
print(array5[2: , :2])

####################################

array6 = np.array([1,2,3,4])

print(array6 + 1)
print(array6 - 2)
print(array6 * 3)
print(array6 / 4)
print(array6 ** 5)

####################################
array7 = np.array([1.43121,2.52323,3.8823,4.3234])

print(np.sqrt(array7))
print(np.round(array7, 2)) # oddiy yaxlitlash.
print(np.floor(array7)) # pastga yaxlitlash.
print(np.ceil(array7)) # yuqoriga yaxlitlash.
print(np.pi)

#######################################
scores = np.array([63, 75, 100, 55, 89])

print(scores > 60) # bool array qaytaradi.
scores[scores < 60] = 0
scores[scores >= 60] = 1
print(scores)

#########################################
array8 = np.array([[1,2,3,4]])
array9 = np.array([[1], [2], [3], [4]])
print(array8.shape,  array9.shape)
print(array8 * array9)
print(array8 / array9)
print(array8 - array9)
print(array8 + array9)

array10 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array11 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(array10*array11)

#########################################
array12 = np.array([[1,2,3,4,5],
                    [6,7,8,9,10],])

print(np.sum(array12))
print(np.min(array12))
print(np.max(array12))
print(np.argmin(array12)) # minumumni indexini qaytaradi.
print(np.argmax(array12)) # maximumni indexini qaytaradi.
print(np.mean(array12))
print(np.std(array12)) # qandaydir statistik malumot.
print(np.var(array12)) # stdning kvadratini qaytaradi.

print(np.sum(array12 , axis=0)) # ustun bo'yicha summa hisoblab list qaytaradi.
print(np.sum(array12 , axis=1)) # qator bo'yicha summa hisoblab list qaytaradi.

#################################
ages = np.array([[31,42,16,25,17,69,33],
                 [21,32,18,16,67,43,20]])

teenagers = ages[ages < 18] # shape buzuladi.
print("Teenagers",teenagers)
adults = ages[(ages >= 18) & (ages < 65)]
print("Adults",adults)
seniors = ages[ages >= 65]
print("Seniors",seniors)

adults2 = np.where(ages > 20, ages, -1) # shape saqlanib qoladi.
print("Adults2\n",adults2)

##################################
rng = np.random.default_rng() # defaultga seed=1 berilsa bitta qiymatni qaytaradi.
print(rng.integers(0, 2 , (3,4))) # size orqali kerakli shape hosil qilsa bo'ldi.

# np.random.seed(seed=1) # bitta qiymat qaytaraveradi.

print(np.random.uniform(1, 5, (2,5)))

array13 = np.array([1,2,3,4,5])
rng.shuffle(array13) # berilgan arraydagi elementlar joyini random qiladi.
print(array13)

fruits = np.array(["apple", "banana", "cherry", "orange"])
fruit = rng.choice(fruits, (2,4))
print(fruit)









