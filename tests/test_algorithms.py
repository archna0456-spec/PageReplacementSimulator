from algorithms.fifo import fifo

pages = [1, 2, 3, 1, 4, 2, 5]
capacity = 3

history, hits, faults = fifo(pages, capacity)

print("FIFO Page Replacement")
print("---------------------")

for step in history:
    print(
        "Page:", step["page"],
        "| Frames:", step["frames"],
        "| Status:", step["status"]
    )

print("\nTotal Hits:", hits)
print("Total Page Faults:", faults)