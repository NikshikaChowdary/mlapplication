# Take input for marks in three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculate the average marks
average = (subject1 + subject2 + subject3) / 3

# Determine the grade based on the average
if average >= 90:
    print("Grade: A")
elif 80 <= average <= 89:
    print("Grade: B")
elif 70 <= average <= 79:
    print("Grade: C")
else:
    print("Grade: Fail")
