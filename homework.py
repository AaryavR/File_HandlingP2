file = open("codingal.txt", "r")
print(file.read())
file.close()

file = open("codingal.txt", "r")
print("Read in parts\n")
print(file.read(18))
file.close()

file = open('codingal.txt', 'r')
print(file.readline())
print(file.readline())
file.close()

file = open('codingal.txt', 'r')
for line in file:
    print(line)
file.close() 

file = open('codingal.txt', 'r')
print(file.readlines())
file.close() 