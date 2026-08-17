# Lesson 06: Combining Logical Operators and Comparison Chaining

temp = 20
is_sunny = True

# Python supports chained comparisons: 0 < temp < 28
if temp >= 28 and is_sunny:
    print("Weather: It is hot and sunny outside.")
elif temp <= 0 and is_sunny:
    print("Weather: It is freezing cold but sunny outside.")
elif 0 < temp < 28 and is_sunny:
    print("Weather: It is pleasantly warm and sunny outside.")
elif temp >= 28 and not is_sunny:
    print("Weather: It is hot and cloudy/rainy outside.")
elif temp <= 0 and not is_sunny:
    print("Weather: It is freezing cold and overcast.")
else:
    print("Weather: Moderate temperatures with cloudy skies.")
