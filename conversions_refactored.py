def convert(value, from_unit, to_unit):
    conversions = {
        ('celsius', 'kelvin'): lambda c: c + 273.15,
        ('celsius', 'fahrenheit'): lambda c: (c * 9/5) + 32,
        ('fahrenheit', 'celsius'): lambda f: (f - 32) * 5/9,
        ('fahrenheit', 'kelvin'): lambda f: (f + 459.67) * 5/9,
        ('kelvin', 'celsius'): lambda k: k - 273.15,
        ('kelvin', 'fahrenheit'): lambda k: (k * 9/5) - 459.67,
        ('miles', 'yards'): lambda m: m * 1760,
        ('miles', 'meters'): lambda m: m * 1609.34,
        ('yards', 'miles'): lambda y: y / 1760,
        ('yards', 'meters'): lambda y: y * 0.9144,
        ('meters', 'miles'): lambda m: m / 1609.34,
        ('meters', 'yards'): lambda m: m / 0.9144,
    }

    key = (from_unit.lower(), to_unit.lower())
    if key in conversions:
        return conversions[key](value)
    else:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

# Example usage:
# result = convert(100, 'celsius', 'fahrenheit')
