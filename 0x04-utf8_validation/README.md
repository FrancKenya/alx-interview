UTF-8 Validation Project
This project is a Python-based utility for validating UTF-8 encoded data. UTF-8 (Unicode Transformation Format - 8-bit) is a character encoding capable of encoding all possible characters (code points) in Unicode. UTF-8 is widely used on the web and is backward-compatible with ASCII, making it ideal for applications requiring internationalization.

Objective
The primary goal of this project is to determine if a dataset, represented by a list of integers, is a valid UTF-8 encoding. Each integer in this list represents a byte of data. The code follows specific encoding rules to assess whether the given data conforms to UTF-8 standards.

How UTF-8 Encoding Works
In UTF-8 encoding, each character can be represented by 1 to 4 bytes. The number of bytes required for each character depends on the value of the Unicode code point for that character. The format of each byte in UTF-8 encoding varies depending on the number of bytes needed:

1-byte character: 0xxxxxxx
Used for ASCII characters (0-127). The leading bit is 0, making it simple to identify.
2-byte character: 110xxxxx 10xxxxxx
Begins with 110 in the first byte, followed by 10 in the subsequent byte(s).
3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
Begins with 1110 in the first byte, followed by two bytes starting with 10.
4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Begins with 11110 in the first byte, followed by three bytes starting with 10.
Each of these patterns has a unique prefix that helps identify the number of bytes a character consists of. If a byte sequence doesn’t follow these patterns, it is considered invalid UTF-8.

Implementation Overview
Validation Steps
Identify the Number of Bytes: For each byte in the dataset, determine if it is the start of a new character. This can be determined by the leading bits:

0xxxxxxx: Indicates a 1-byte (ASCII) character.
110xxxxx: Indicates the start of a 2-byte character.
1110xxxx: Indicates the start of a 3-byte character.
11110xxx: Indicates the start of a 4-byte character.
Validate Continuation Bytes: If the initial byte signifies a multi-byte character, ensure that the following bytes start with 10. These are known as continuation bytes, and each one should follow the pattern 10xxxxxx.

Final Check: After iterating through the dataset, confirm that all characters are complete. If any multi-byte character lacks the required continuation bytes, the sequence is invalid.

Bitwise Operations
Bitwise operations are essential for decoding UTF-8 bytes efficiently. Here’s a quick overview of the bitwise operations used in the validation logic:

Masking: Used to isolate specific bits and check the byte’s leading bits.
Bitwise AND (&): Applied to mask specific bits of a byte. For example, byte & 0b11100000 isolates the three leading bits of a byte.
Shifting: (Not explicitly used here but commonly useful) involves moving bits left or right to align them for comparisons.
Code Requirements
The Python script follows strict coding guidelines:

Interpreted on Ubuntu 20.04 LTS using Python 3.4.3
Follows PEP 8 style (version 1.7.x)
Each file ends with a new line and starts with the #!/usr/bin/python3 interpreter directive
Code is executable and well-documented

Project Structure
Main Script: Contains the core function, validUTF8(data), which performs UTF-8 validation.
Documentation: Includes comments and descriptions explaining each part of the code, making the validation logic clear.

Conclusion
This project provides a foundational understanding of UTF-8 validation and demonstrates how Python’s bitwise operations can facilitate efficient data encoding checks. The logic built here can be expanded to validate other encoding schemes or serve as a backend utility in larger applications that need to support international text.
