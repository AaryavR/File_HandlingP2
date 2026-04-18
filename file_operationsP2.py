file = open("codingal.txt", "r")
print("File is in read mode")
file.close()

file = open("codingal.txt", "w")
file.write("Hi I am Aaryav and I am 15")
file.close()

file = open("codingal.txt", "a")
file.write("This is appended")
file.close()
