import matplotlib.pyplot as plt

filenames = ['8_01.txt'] #, '8_02.txt', '8_03.txt',
           # '8_04.txt', '8_05.txt', '8_06.txt',
           # '8_07.txt', '8_08.txt', '8_09.txt',
           # '8_10.txt']

for filename in filenames:
    x_l = []
    y_l = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            result = [int(x) for x in line.strip("\n").split(",")]
            x_l.append(result[0])
            y_l.append(result[1])
            #l.append(line.strip("\n").split(","))

#plt.plot(x_l,y_l,'bo')
title = "Historgram of 3x+1 on " + str(filename)
plt.xlabel = ("Steps")
plt.ylabel = ("Prime Number")
plt.title = title
#plt.axis([min(x_l),max(x_l)])
plt.hist(y_l,40)
plt.show()
