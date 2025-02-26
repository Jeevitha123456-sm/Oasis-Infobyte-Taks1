def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

def main():
    # Get user input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Output result
    print(f"Your BMI is: {bmi:.2f}")
    
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
        
    print(f"You are classified as: {category}")
    
if __name__ == "__main__":
    main()

