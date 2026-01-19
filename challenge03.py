def broadcast(num_users, max_msgs, actions):
    followers = [set() for _ in range(num_users + 1)]
    inbox = [[] for _ in range(num_users + 1)]
    global_msg_id = 0

    for act in actions:
        parts = act.split()

        if parts[0] == 'S':
            sender, target = int(parts[1]), int(parts[2])
            followers[sender].add(target)

        elif parts[0] == 'U':
            sender, target = int(parts[1]), int(parts[2])
            followers[sender].discard(target)

        elif parts[0] == 'B':
            user, msg_val = int(parts[1]), int(parts[2])
            global_msg_id += 1
            important = (msg_val % 3 == 0)

            inbox[user].append((global_msg_id, important))
            if len(inbox[user]) > max_msgs:
                inbox[user].pop(0)

        elif parts[0] == 'F':
            user = int(parts[1])
            feed = []

            feed.extend(inbox[user])
            for f in followers[user]:
                feed.extend(inbox[f])

            if not feed:
                print("EMPTY")
                continue

            feed.sort(key=lambda x: (-x[0], -x[1]))

            top_messages = [str(mid) for mid, _ in feed[:10]]
            print(" ".join(top_messages))


num_users = 3
max_msgs = 2
actions = [
    "S 1 2",
    "S 1 3",
    "B 2 5",
    "B 3 9",
    "F 1",
    "U 1 2",
    "B 3 6",
    "F 1",
    "F 2"
]

broadcast(num_users, max_msgs, actions)
