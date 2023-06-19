import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return math.pi * 2 * radius

url = "https://www.google.com"
dburl2 = "jdbc:mysql://localhost:3306/test"

def creds_store():
    return creds = {
        "url": "http://www.google.com",
        "dbUrl" : "jdbc:mysql://localhost:3306/test",
        "user": "sqladminuser",
        "password": "Apr2022th"
    }

def main(radius):
    try:
        radius = float(radius)
        if radius<=0:
            raise ValueError
    except ValueError:
        print("Please enter a valid number for radius")
        return

    area = calculate_area(radius)
    circumference = calculate_circumference(radius)

    print("Area of circle is : ", area)
    print("Circumference of circle is : ", circumference)
