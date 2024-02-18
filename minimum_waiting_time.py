def minimum_waiting_time(patients):
    patients.sort()  # Sort the list of patients in ascending order of treatment time
    total_waiting_time = 0
    for i in range(len(patients)):
        waiting_time = patients[i] * (len(patients) - i - 1)
        total_waiting_time += waiting_time
    return total_waiting_time

# Example usage:
patients = [5, 2, 1, 3]
print("Minimum total waiting time:", minimum_waiting_time(patients))
