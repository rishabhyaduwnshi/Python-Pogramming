import heapq
H = []

heapq.heappush(H,20);
heapq.heappush(H,50);
heapq.heappush(H,10);
print(H)

heapq.heappop(H)
print(H)


my_list = [10,30,20,60,50]
heapq.heapify(my_list)
print(my_list)
