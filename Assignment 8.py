n = int(input())
trains = []

for idx in range(n):
    line = input()
    name = line.split()[0]

    time_str = line.split()[-1]

    h, m = time_str.split(":")
    time_in_minutes = int(h) * 60 + int(m)
    trains.append((name, time_in_minutes, idx, line))

for i in range(n - 1):
    mIndex = i
    for j in range(i + 1, n):
        if trains[j][0] < trains[mIndex][0]:
            mIndex = j
        elif trains[j][0] == trains[mIndex][0]:
            if trains[j][1] > trains[mIndex][1]:
                mIndex = j
            elif trains[j][1] == trains[mIndex][1]:
                if trains[j][2] < trains[mIndex][2]:
                    mIndex = j
    if mIndex != i:
        trains[i], trains[mIndex] = trains[mIndex], trains[i]

for t in trains:
    print(t[3])