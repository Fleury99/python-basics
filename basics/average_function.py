def average(grades_list):
    # Security: if the list is empty, return 0 to prevent a division by zero
    if len(grades_list) == 0:
        return 0
    # Calculate the total sum of all grades in the list
    total_sum = sum(grades_list)

    # Count the total number of grades available
    total_elements = len(grades_list)

    # Compute the final average by dividing the sum by the count
    average = total_sum / total_elements

    # Return the calculated average score to the caller
    return average

# Example usage
student_grades =[12, 15, 18, 10, 14]

student_average = average(student_grades)

# Debug checks
print(f"Total sum of grades: {sum(student_grades)}")
print(f"Total number of grades: {len(student_grades)}")

# Final output

print(f"The student average is: {student_average}")
