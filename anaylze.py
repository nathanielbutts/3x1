filenames = ['8_01.txt', '8_02.txt', '8_03.txt',
            '8_04.txt', '8_05.txt', '8_06.txt',
            '8_07.txt', '8_08.txt', '8_09.txt',
            '8_10.txt']

l = []
outlist = []
for filename in filenames:
    l = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            result = [int(x) for x in line.strip("\n").split(",")]
            l.append(result)
            #l.append(line.strip("\n").split(","))

    idx, max_value = max(l, key = lambda item: item[1])
    outlist.append(idx)
    outlist.append(max_value)
    print(max_value, idx)

idx, max_value = max(outlist, key = lambda item: item[1])
print(max_value, idx)