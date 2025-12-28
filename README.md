# Gregorian to Jalali Converter

A simple Python utility to convert Gregorian dates (`yyyy/mm/dd`) to Jalali (Persian) calendar dates (`yyyy/mm/dd`) with zero-padded formatting. 

## Features

- No external libraries required.
- Correctly handles leap years.
- Zero-padded output: `1404/10/07`.

## Usage

```python
date = "2025/12/28"
jalali_date = convert_to_persian(date)
print(jalali_date)  # Output: 1404/10/07
```
