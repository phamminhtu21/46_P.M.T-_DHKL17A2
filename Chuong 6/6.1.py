import threading

def print_thread_name():
    print(f"Thread name: {threading.current_thread().name}")
num_threads = 5
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=print_thread_name, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print("Tất cả đã được in.")
