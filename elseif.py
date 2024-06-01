iterations = 100000

file = open("thethingy.lua", "w")

string = 'if x == 1 then\n    print("x is odd")\n'

for i in range(2,iterations,1):
    if i%2 == 0:
        string += 'elseif x == '+str(i)+' then\n    print("x is even")\n'
    else:
        string += 'elseif x == '+str(i)+' then\n    print("x is odd")\n'	
    print(i)	

if (iterations)%2 == 0:
    string += 'elseif x == '+str(iterations)+' then\n    print("x is even")\nend'
else:
    string += 'elseif x == '+str(iterations)+' then\n    print("x is odd")\nend'

file.write(string)
file.close()

print("the program has finished")
