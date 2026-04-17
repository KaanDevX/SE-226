import geometry_utils

def main():
    area_functions = {
        "circle": geometry_utils.circle_area,
        "rectangle": geometry_utils.rectangle_area,
        "triangle": geometry_utils.triangle_area
    }

    print("--- Shape Area Calculator ---")
    shape = input("Enter the shape type (circle, rectangle, or triangle): ").strip().lower()

    if shape not in area_functions:
        print("Error: Invalid shape type. Please choose circle, rectangle, or triangle.")
        return

    if shape == "circle":
        radius = float(input("Enter the radius: "))
        result = area_functions[shape](radius)

    elif shape == "rectangle":
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        result = area_functions[shape](width, height)

    elif shape == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        result = area_functions[shape](base, height)

    if isinstance(result, str):
        print(result)
    else:
        print(f"The area of the {shape} is: {result}")

if __name__ == "__main__":
    main()