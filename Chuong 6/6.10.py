import threading
import random

def find_max_sublist(sublist, result, index):
    result[index] = max(sublist)
n = 100
num_threads = 4
data = [random.randint(0, 100) for _ in range(n)]
chunk_size = len(data) // num_threads
sublists = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
results = [0] * num_threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=find_max_sublist, args=(sublists[i], results, i))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
max_value = max(results)
print(f"Giá trị lớn nhất trong dsach: {max_value}")
