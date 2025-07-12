N=int(input())
st_id=[int(x) for x in input().split()]
mark=[int(y) for y in input().split()]
swaps = 0

for i in range(N - 1):
    m_x = i
    for j in range(i + 1, N):
        if mark[j] > mark[m_x] or (mark[j] == mark[m_x] and st_id[j] < st_id[m_x]):
            m_x = j
    if m_x != i:
        mark[i], mark[m_x] = mark[m_x], mark[i]
        st_id[i], st_id[m_x] = st_id[m_x], st_id[i]
        swaps += 1
print("Minimum swaps: " + str(swaps))

for j in range(N):
    print("ID: " + str(st_id[j]) + " Mark: " + str(mark[j]))