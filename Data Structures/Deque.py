from collections import deque
my_list = [1,2,3,4,5]

dq = deque(my_list)

#adding element from right
dq.append(6)
print(dq)

#appending element from left
dq.appendleft(0)
print(dq)

#deleting from right side
dq.pop()
print(dq)

#deleting from left side
dq.popleft()
print(dq)
