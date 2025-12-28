# Gregorian to Jalali Converter

A simple Python utility to convert Gregorian dates (`yyyy/mm/dd`) to Jalali (Persian) calendar dates (`yyyy/mm/dd`) with zero-padded formatting. 

## Features

- No external libraries required.
- Correctly handles leap years.
- Zero-padded output: `1385/05/11`.

## Usage

```python
from convert import convert_to_persian

date = "2006/08/01"
jalali_date = convert_to_persian(date)
print(jalali_date)  # Output: 1385/05/11
