import json

with open('skeleton.json','r') as skeletonFile:
    data = json.load(skeletonFile)

index = 4
end = ""
flag = []

while end != "}":
    if index == 120:
        toCompare = data[1][1][index+2][0]
    else:
        toCompare = data[1][1][index+3][0]
    for x in data[1][1][index][4][0][1]:
        if x[2] == toCompare:
            flag.append(x[0])
            if x[0] == "}":
                end = "}"
            break
    index+=4

print("".join(flag))