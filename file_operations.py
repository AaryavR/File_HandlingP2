file = open("codingal.txt", "r")
print(file.read())
file.close()

file = open("codingal.txt", "r")
print("Read in parts\n")
print(file.read(18))
file.close()

file = open("codingal.txt", "a")
file.write("Hi I am Aaryav and I am 15")
file.close() 