from itertools import chain

def ConquestCampaign(n, m, l, battalion):
    a = [[0] * m for i in range(n)]
    x = [[battalion[i] - 1, battalion[i+1] - 1] for i in range(2*l) if i % 2 == 0]

    day = 0
    y = x.copy()
    while not all(list(chain(*a))):
        print(a)
        for i in x:
            a[i[0]][i[1]] = 1

            if i[0] == 0 and i[1] == 0:
                if [i[0]+1, i[1]] not in y:
                    y.append([i[0]+1, i[1]])
                if [i[0], i[1]+1] not in y:
                    y.append([i[0], i[1]+1])

            elif i[0] == 0 and i[1] != 0 and i[1] != (len(a[1]) - 1):
                if [i[0], i[1] + 1] not in y:
                    y.append([i[0], i[1]+1])
                if [i[0], i[1] - 1] not in y:
                    y.append([i[0], i[1]-1])
                if [i[0] + 1, i[1]] not in y:
                    y.append([i[0]+1, i[1]])

            elif i[0] != 0 and i[1] == 0 and i[0] != (len(a) - 1):
                if [i[0], i[1] + 1] not in y:
                    y.append([i[0], i[1]+1])
                if [i[0] + 1, i[1]] not in y:
                    y.append([i[0]+1, i[1]])
                if [i[0] - 1, i[1]] not in y:
                    y.append([i[0]-1, i[1]])

            elif i[0] == 0 and i[1] == (len(a[1]) - 1):
                if [i[0], i[1] - 1] not in y:
                    y.append([i[0], i[1] - 1])
                if [i[0] + 1, i[1]] not in y:
                    y.append([i[0] - 1, i[1]])

            elif i[0] == (len(a) - 1) and i[1] == 0:
                if [i[0] - 1, i[1]] not in y:
                    y.append([i[0]+1, i[1]])
                if [i[0], i[1] + 1] not in y:
                    y.append([i[0], i[1]+1])

            elif i[0] == (len(a) - 1) and i[1] == (len(a[1]) - 1):
                if [i[0] - 1, i[1]] not in y:
                    y.append([i[0]-1, i[1]])
                if [i[0], i[1] - 1] not in y:
                    y.append([i[0], i[1]-1])

            elif i[0] != (len(a) - 1) and i[1] == (len(a[1]) - 1):
                if [i[0], i[1] - 1] not in y:
                    y.append([i[0], i[1]-1])
                if [i[0] + 1, i[1]] not in y:
                    y.append([i[0]+1, i[1]])
                if [i[0] - 1, i[1]] not in y:
                    y.append([i[0]-1, i[1]])

            elif i[0] == (len(a) - 1) and i[1] != (len(a[1]) - 1):
                if [i[0], i[1] + 1] not in y:
                    y.append([i[0], i[1]+1])
                if [i[0], i[1] - 1] not in y:
                    y.append([i[0], i[1]-1])
                if [i[0] - 1, i[1]] not in y:
                    y.append([i[0]-1, i[1]])

            else:
                if [i[0], i[1] + 1] not in y:
                    y.append([i[0], i[1]+1])
                if [i[0], i[1] - 1] not in y:
                    y.append([i[0], i[1]-1])
                if [i[0] + 1, i[1]] not in y:
                    y.append([i[0]+1, i[1]])
                if [i[0] - 1, i[1]] not in y:
                    y.append([i[0]-1, i[1]])

        x = []
        x = x + y
        print(x)
        day += 1

    for i in a:
        print(''.join(str(i)))

    print(day)

print(ConquestCampaign(2, 2, 2, [2, 2, 2, 2]))



