class Patient:
     def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency




class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = (
                    self.data[parent], self.data[index]
                )
                index = parent
            else:
                break


    def heapify_down(self, index):
        size = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left

            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest], self.data[index]
            )
            index = smallest

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if len(self.data) == 0:
            return None

        return self.data[0]

    def remove_min(self):
        if len(self.data) == 0:
            return None

        min_patient = self.data[0]
        last_patient = self.data.pop()

        if len(self.data) > 0:
            self.data[0] = last_patient
            self.heapify_down(0)

        return min_patient


# Test your MinHeap class here including edge cases

# Test the emergency priority queue
heap = MinHeap()

heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))

print("\nOriginal Queue:")
heap.print_heap()

print("\nNext Patient:")
next_up = heap.peek()
print(next_up.name, next_up.urgency)

print("\nRemoving Most Urgent Patient:")
served = heap.remove_min()
print(served.name)
heap.print_heap()

# Test empty queue
print("\nTesting Empty Queue:")
empty_heap = MinHeap()
print(empty_heap.peek())
print(empty_heap.remove_min())

# Test a queue with one patient
print("\nTesting One Patient:")
single_heap = MinHeap()
single_heap.insert(Patient("Riley", 2))
print(single_heap.remove_min().name)
print(single_heap.peek())

