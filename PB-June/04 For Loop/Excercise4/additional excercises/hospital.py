#  Input
period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

#  Logic
for day in range(1, period + 1):
    patients_count = int(input())
    if day % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if patients_count <= doctors:
        treated_patients += patients_count
    else:
        treated_patients += doctors
        untreated_patients += (patients_count - doctors)


#  Print Output

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')

