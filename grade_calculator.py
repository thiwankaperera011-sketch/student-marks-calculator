def calculate_grade(marks):
    if marks >= 75:
        return 'A (Distinction)'
    elif marks >= 65:
        return 'B (Very Good Pass)'
    elif marks >= 50:
        return 'C (Credit Pass)'
    elif marks >= 35:
        return 'S (Ordinary Pass)'
    else:
        return 'F (Weak / Fail)'

def main():
    print("--- Student Marks & Grade Calculator ---")
    name = input("Enter Student Name: ")
    
    try:
        it_marks = float(input("Enter IT Marks: "))
        tech_marks = float(input("Enter Engineering Tech Marks: "))
        sft_marks = float(input("Enter Science for Tech Marks: "))
        
        total = it_marks + tech_marks + sft_marks
        average = total / 3
        
        print("\n--- Results Summary ---")
        print(f"Student Name: {name}")
        print(f"Total Marks: {total:.2f}")
        print(f"Average Marks: {average:.2f}")
        print(f"IT Grade: {calculate_grade(it_marks)}")
        print(f"Engineering Tech Grade: {calculate_grade(tech_marks)}")
        print(f"Science for Tech Grade: {calculate_grade(sft_marks)}")
        
    except ValueError:
        print("Please enter valid numeric values for marks!")

if __name__ == "__main__":
    main()