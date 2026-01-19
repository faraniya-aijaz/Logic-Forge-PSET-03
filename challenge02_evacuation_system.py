def rescue_operation(people_weights, is_priority, max_limit, queries):
    total = len(people_weights)

    # Separate priority and regular evacuees
    priority_list = []
    regular_list = []

    for idx in range(total):
        if is_priority[idx] == 1:
            priority_list.append(people_weights[idx])
        else:
            regular_list.append(people_weights[idx])

    priority_list.sort()
    regular_list.sort()

    boat_count = 0
    left = 0
    right = len(regular_list) - 1

    # Try pairing priority with regular if possible
    for w in priority_list:
        while right >= left and regular_list[right] + w > max_limit:
            right -= 1

        if right >= left:
            right -= 1  # successfully paired
        boat_count += 1  # priority person always uses a boat

    # Remaining regular people
    remaining_people = right - left + 1
    boat_count += (remaining_people + 1) // 2

    # --- Handle Queries ---
    output = []

    for q in queries:
        parts = q.split()

        if parts[0] == "CANPAIR":
            a, b = int(parts[1]), int(parts[2])
            if people_weights[a] + people_weights[b] <= max_limit and not (is_priority[a] == 1 and is_priority[b] == 1):
                output.append("Yes")
            else:
                output.append("No")

        elif parts[0] == "REMAINING":
            max_boats = int(parts[1])
            evac_possible = min(total, 2 * max_boats)
            output.append(str(total - evac_possible))

    return boat_count, output


# --- Example Usage ---
people_weights = [30, 50, 60, 40, 70, 80]
is_priority = [1, 0, 1, 0, 0, 1]
max_limit = 100

queries = [
    "CANPAIR 0 1",
    "CANPAIR 0 2",
    "REMAINING 2"
]

boats_needed, answers = rescue_operation(people_weights, is_priority, max_limit, queries)

print("Minimum boats =", boats_needed)
for ans in answers:
    print(ans)
