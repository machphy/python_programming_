def celsius_to_fahrenheit(celsius):
    """Celsius को Fahrenheit में convert करता है"""
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """Celsius को Kelvin में convert करता है"""
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """Fahrenheit को Celsius में convert करता है"""
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    """Kelvin को Celsius में convert करता है"""
    return kelvin - 273.15

# Temperature Conversion Program
print("=" * 40)
print("Temperature Converter")
print("=" * 40)

# Example conversions
temp_c = 25
print(f"\n{temp_c}°C = {celsius_to_fahrenheit(temp_c):.2f}°F")
print(f"{temp_c}°C = {celsius_to_kelvin(temp_c):.2f}K")

temp_f = 77
print(f"\n{temp_f}°F = {fahrenheit_to_celsius(temp_f):.2f}°C")

temp_k = 298.15
print(f"\n{temp_k}K = {kelvin_to_celsius(temp_k):.2f}°C")

print("\n" + "=" * 40)
