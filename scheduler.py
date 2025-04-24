import heapq

def schedule(tasks):
    tasks.sort(key=lambda x: x[1])
    current_time = 0
    index = 0
    waiting_tasks = []
    execution_order = []

    while index < len(tasks) or waiting_tasks:
        while index < len(tasks) and tasks[index][1] <= current_time:
            task_id, arrival, priority, duration = tasks[index]
            heapq.heappush(waiting_tasks, (priority, arrival, task_id, duration))
            index += 1

        if waiting_tasks:
            priority, arrival, task_id, duration = heapq.heappop(waiting_tasks)
            execution_order.append(task_id)
            current_time += duration
            current_time += 1
        else:
            if index < len(tasks):
                current_time = tasks[index][1]
            else:
                break

    return execution_order

tasks = [
    (1, 0, 2, 3),
    (2, 2, 1, 2),
    (3, 4, 3, 1)
]

print(schedule(tasks))
tasks1 = [
    [1, 0, 2, 3],
    [2, 1, 2, 2],
    [3, 2, 1, 5],
    [4, 5, 1, 2]
]
print(schedule(tasks1))  

tasks2 = [
    [1, 0, 1, 4],
    [2, 1, 3, 2],
    [3, 2, 2, 1],
    [4, 3, 1, 3]
]
print(schedule(tasks2))  

tasks3 = [
    [1, 0, 1, 2],
    [2, 5, 2, 3],
    [3, 6, 2, 1],
    [4, 7, 1, 2]
]
print(schedule(tasks3))  
