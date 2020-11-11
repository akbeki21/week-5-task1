import json
# Task 1
# with open ('task.txt', 'r') as file :
#     for line in file.readlines() :

#         if '1' in line :
#             print (line)
#         elif '2' in line :
#             print (line)    


# with open ('task.txt', 'r') as f :
#     nums = [x for x in f.read().split()]
#     ball = []
#     for num in nums :
#         if num.isdigit():
#             ball.append(int(num))

#     res = int(sum(ball) / len(ball))

#     print(f'Средний балл класса : {res}')



# Task 2
# some_text = input("Type: ")
# file = open('some_text', "w")

# while True:
#     text = input()
#     if text == "":
#         break
#     file.write(text+'\n')

# file.close()
# print(some_text)



# Task 3
# file = open("task.txt", "r+")
# print(f' Количество строк равно  {len(file.readlines())}')



# Task 4
# file = open('nums.txt', "r+")

# num = file.read()
# num = num.split()

# for x in range(len(num)):
#     num[x] = int(num[x])
# file.close()
# print(sum(num))



# Task 5
# from functools import reduce

# with open ('input.txt', 'r') as file :
#     line_num = 1
#     with open ('output.txt', 'w+') as f :
#         for line in file.readlines():
#             nums = list(map(int, line.split()))
#             res = reduce(lambda x, y: x * y, nums)
            
#             f.writelines('Произведение чисел '+ str(line_num) + ' строки - ' + str(res) + str('\n'))
#             line_num += 1



# Task 8
# str_ = { "name":"John", "age":30, "city":"New York"}
# with open ('json_', 'r+') as f :

#     data = json.load(f)
#     print(data['age'])



# Task 9
# file = open("dict_", 'w')

# some_dict = {
#     "name": "John", "age": 30, "city": "NY"
#     }

# json.dump(some_dict, file)
# file.close()