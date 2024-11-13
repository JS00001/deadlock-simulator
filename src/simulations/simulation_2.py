from ..utils.deadlock_detector import DeadlockDetector

def simulation_2():
    detector = DeadlockDetector()

    # Allocate resources to processes
    detector.allocate_resource(1, 1)
    detector.allocate_resource(2, 2)
    detector.allocate_resource(3, 3)

    # Request resources
    detector.request_resource(1, 2)
    detector.release_resource(2, 2)  # Process 2 releases its allocated resource
    detector.request_resource(2, 3)
    detector.request_resource(3, 1)

    # Non-Deadlock State: 1 is waiting for 2, it gets 2, 2 is waiting for 3, 3 is waiting for 1, which is released
    deadlocked = detector.detect_deadlock()

    if deadlocked:
        print("Deadlock detected!")
        detector.resolve_deadlock(deadlocked)
    else:
        print("No deadlock detected")