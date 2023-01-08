import re

def f(player1, player2):
    
    x1 = re.findall(r"[a-zA-Z]", player1)
    y1 = re.findall(r"\d", player1)
    sum1 = 0

    x2 = re.findall(r"[a-zA-Z]", player2)
    y2 = re.findall(r"\d", player2)
    sum2 = 0

    sum1 += 10*(len(x1))

    for i in range(0, len(y1)):
        if y1[i] == "1":
            sum1 += 10
            i = i + 1
        else:
            sum1 += int(y1[i])

    sum2 += 10*(len(x2))

    for i in range(0, len(y2)):
        if y2[i] == "1":
            sum2 += 10
            i = i + 1
        else:
            sum2 += int(y2[i])

    if(sum1>sum2):
        return True
    else:
        return False