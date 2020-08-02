def SynchronizingTables(n, ids, salary):
    new_ids = ids.copy()
    new_ids.sort()
    salary.sort()
    table = dict(zip(new_ids, salary))
    y = []
    for j in ids:
        for i in table.items():
            print(i)
            print(j)
            if j == i[0]:
                y.append((i[1]))

    return(y)

