class Proc:
    def __init__(self, pid, name, start, prio):
        self.pid = pid
        self.name = name
        self.start = start
        self.prio = prio

def print_table(procs):
    print("PID\tName\tStart\tPrio")
    for proc in procs:
        print(f"{proc.pid}\t{proc.name}\t{proc.start}\t\t{proc.prio}")

def bubble_sort(procs, key_func):
    n = len(procs)
    for i in range(n):
        for j in range(0, n-i-1):
            if key_func(procs[j]) > key_func(procs[j+1]):
                procs[j], procs[j+1] = procs[j+1], procs[j]

def sort_by_pid(procs):
    bubble_sort(procs, lambda proc: proc.pid)

def sort_by_start(procs):
    bubble_sort(procs, lambda proc: proc.start)

def sort_by_prio(procs):
    prio_order = {"Low": 1, "MID": 2, "High": 3}
    bubble_sort(procs, lambda proc: prio_order[proc.prio])

def main():
    procs = [
        Proc("P1", "VSCode", 100, "MID"),
        Proc("P23", "Eclipse", 234, "MID"),
        Proc("P93", "Chrome", 189, "High"),
        Proc("P42", "JDK", 9, "High"),
        Proc("P90", "CMD", 7, "High"),
        Proc("P87", "NotePad", 23, "Low")
    ]

    print("Choose sorting parameter:")
    print("1. Sort by PID\n2. Sort by Start\n3. Sort by Prio")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        sort_by_pid(procs)
    elif choice == 2:
        sort_by_start(procs)
    elif choice == 3:
        sort_by_prio(procs)
    else:
        print("Invalid choice.")
        return

    print_table(procs)

if __name__ == "__main__":
    main()

