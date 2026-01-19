def city_alerts(temp, K):
    n = len(temp)
    up = [-1] * n
    down = [-1] * n
    st = []

    for i in range(n):
        while st and temp[i] >= temp[st[-1]] + K:
            up[st.pop()] = i
        st.append(i)

    st = []

    for i in range(n):
        while st and temp[i] <= temp[st[-1]] - K:
            down[st.pop()] = i
        st.append(i)

    alert = [0] * n
    INF = 10**9

    for i in range(n):
        a = up[i] if up[i] != -1 else INF
        b = down[i] if down[i] != -1 else INF
        best = min(a, b)
        alert[i] = best if best != INF else 0

    return alert

temp = [73, 74, 75, 71, 69, 72, 76, 73]
K = 2
alerts = city_alerts(temp, K)
print(alerts)
print(alerts[3])
count_nonzero = sum(1 for i in range(0, 8) if alerts[i] != 0)
print(count_nonzero)

temp = [30, 31, 29, 35]
K = 3
alerts = city_alerts(temp, K)
print(alerts)

temp = [10, 20, 15]
K = 5
alerts = city_alerts(temp, K)
print(alerts)
