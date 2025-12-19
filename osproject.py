def fifo(pages, frames):
    memory = []
    page_faults = 0

    print("\nFIFO Page Replacement\n")

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        print("Page:", page, "Frames:", memory)

    print("\nTotal Page Faults:", page_faults)


def lru(pages, frames):
    memory = []
    page_faults = 0

    print("\nLRU Page Replacement\n")

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)

        print("Page:", page, "Frames:", memory)

    print("\nTotal Page Faults:", page_faults)



print("Dynamic Memory Management Visualizer")

frames = int(input("Enter number of frames: "))
pages = list(map(int, input("Enter page reference string: ").split()))

print("\nChoose Page Replacement Algorithm")
print("1. FIFO")
print("2. LRU")

choice = int(input("Enter choice: "))

if choice == 1:
    fifo(pages, frames)
elif choice == 2:
    lru(pages, frames)
else:
    print("Invalid choice")