iterations = 10000000

file = open("thethingy.lua", "w")

file.write("")

file.close()

file = open("thethingy.lua", "a")

string = 'if x == 1 then\n    print("x is odd")\n'

for i in range(2,iterations,1):
    if i%2 == 0:
        string += 'elseif x == '+str(i)+' then\n    print("x is even")\n'
    else:
        string += 'elseif x == '+str(i)+' then\n    print("x is odd")\n'

    if i%1000 == 0:
        print(i)
        file.write(string)
        string = ""

if (iterations)%2 == 0:
    string += 'elseif x == '+str(iterations)+' then\n    print("x is even")\nend'
else:
    string += 'elseif x == '+str(iterations)+' then\n    print("x is odd")\nend'

file.write(string)
file.close()

string = ""

print("the program has finished")
