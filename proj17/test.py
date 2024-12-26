import time

from main import edmonds_karp


def generate_large_network(size, capacity):
    network = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            if i != j:
                network[i][j] = capacity // 2
    return network

def performance_test():
    sizes = [10, 50, 100, 200]
    for size in sizes:
        capacity = generate_large_network(size, 100)
        source, sink = 0, size - 1
        start_time = time.time()
        max_flow = edmonds_karp(capacity, source, sink)
        end_time = time.time()
        print(f"Graph size: {size}x{size}, Max flow: {max_flow}, Execution time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    print("Running performance tests for Edmonds-Karp algorithm...")
    performance_test()
