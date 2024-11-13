
from ..utils.deadlock_detector import DeadlockDetector

def simulation_1() :
    detector = DeadlockDetector()

    # Allocate each process to its matching resource
    detector.allocate_resource(1, 1)
    detector.allocate_resource(2, 2)
    detector.allocate_resource(3, 3)

    # Request resources
    detector.request_resource(1, 2)
    detector.request_resource(2, 3)
    detector.request_resource(3, 1)

    # Deadlock State: 1 is waiting for 2, 2 is waiting for 3, 3 is waiting for 1
    deadlocked = detector.detect_deadlock()
    
    if deadlocked:
        print("Deadlock detected!")
        victim = detector.resolve_deadlock(deadlocked)
        print(f"Deadlocked resolved by releasing resource {victim}")
    else:
        print("No deadlock detected")
