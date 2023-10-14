from problems import problem1, problem2, problem3

isuNumber = 409606  # 409606 - 4 2 1 1
print("ISU % 6 = " + str(isuNumber % 6))  # 4
print("ISU % 4 = " + str(isuNumber % 4))  # 2
print("ISU % 7 = " + str(isuNumber % 7))  # 1
print("ISU % 5 = " + str(isuNumber % 5))  # 1

task = input("Enter task number (1-3) you want to run: ")
if task == '1':
    print(problem1.solve(input("Enter your string to find the number of emoticons: ")))
elif task == '2':
    print(problem2.solve(input("Enter your string to find duplicated words: ")))
elif task == '3':
    print(problem3.solve(input("Enter your string to find words with one vowel letter: ")))
else:
    print("Can't resolve task number")
