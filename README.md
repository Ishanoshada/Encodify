# Encodify - Python Code Encoding Module

![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)

`encodify` is a powerful Python module designed to provide a suite of advanced encoding techniques for Python scripts. These encoding methods encompass compression, base64 encoding, and XOR encryption, allowing users to obfuscate code for enhanced security or distribution.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Importing the Module](#importing-the-module)
  - [Creating an Encoder Instance](#creating-an-encoder-instance)
  - [Encoding Specific Code](#encoding-specific-code)
  - [Generating Random Payload](#generating-random-payload)
  - [Generating Payload with a Specific Encoding Method](#generating-payload-with-a-specific-encoding-method)
  - [Additional Customization](#additional-customization)
- [Advanced Techniques](#advanced-techniques)
- [Examples](#examples)
- [Best Practices and Considerations](#best-practices-and-considerations)
- [License](#license)

## Installation

To integrate `encodify` into your project, you can use `pip`:

```bash
pip install encodify
```

## Usage

### Importing the Module

To employ the functionalities of `encodify`, import the `Encodify` class from the module:

```python
from encodify import Encodify
```

### Creating an Encoder Instance

Instantiate the `Encodify` class to access a wide array of encoding techniques:

```python
encoder = Encodify()
```

### Encoding Specific Code

`encodify` excels at encoding specific Python code snippets. For instance, utilizing the `m1` encoding method:

```python
code_to_encode = "print('Hello, World!')"
encoded_code = encoder.m1(code_to_encode)
```

### Generating Random Payload

For a dynamically selected encoding method, use the `random_payload` method. It produces a randomized payload, increasing the level of code obfuscation:

```python
random_payload = encoder.random_payload("print('Hello, World!')", 2)
```

### Generating Payload with a Specific Encoding Method

Tailor the encoding method to your requirements with the `gen_payload` method. Specify the method number to achieve the desired encoding:

```python
# Choose the encoding method (e.g., m2)
chosen_encoding_method = 2
payload = encoder.gen_payload(chosen_encoding_method, "print('Hello, World!')")
```

### Additional Customization

`encodify` offers extensive customization options. These include string replacements and appending/prepending custom code to the encoded output, allowing for fine-tuned control over the obfuscation process.

### Args for `gen_payload` Function

The `gen_payload` function accepts the following arguments:

- `choice` (int): The chosen encoding technique, determining the applied encoding method. Refer to the module documentation for a complete list of available choices.

- `data` (str): The Python code to be encoded.

- `line` (int, optional): The number of lines for line-based encoding (default is 2). This argument is applicable for specific encoding methods.

- `options` (dict, optional): Further customization options (default is None). This may encompass string replacements or the addition of custom code.

### Available Encoding Methods

```plaintext
+------+---------------------------------------------------+
|  No  |           Encoding Method Description            |
+------+---------------------------------------------------+
|  1   |              m1: Gzip + Marshal + Base64          |
|  2   |          m2: LZMA + Base64 + Marshal              |
|  3   |         m3: LZMA + Base85 + Marshal               |
|  4   |              m4: LZMA + Marshal                   |
|  5   |          m5: Base64 + LZMA + Marshal              |
|  6   |       m6: LZMA + Zlib + Marshal + Base64         |
|  7   |     m7: LZMA + Gzip + Marshal + Base64           |
|  8   |              m8: LZMA + Marshal                   |
|  9   |       m9: Base64 + Gzip + Marshal + Base64        |
|  10  |      m10: Base64 + Gzip + Marshal + LZMA          |
|  11  |     m11: Base64 + Gzip + Marshal + Base64         |
|  20  |     m20: Minify + Base64 + Gzip + Marshal         |
|  23  |      l1: Line-based Encoding with Base85          |
|  24  |  l2: Line-based Encoding with Base85 + LZMA       |
|  25  |  l25: Line-based Encoding with Base64 + LZMA      |
|  26  | l26: Line-based Encoding with Base64 + Codecs     |
|  27  |  l27: Line-based Encoding with XOR Encryption     |
|  28  | l28: Line-based Encoding with Base64 + XOR        |
|  29  | l29: Line-based Encoding with Base64 + XOR        |
|  30  | l30: Line-based Encoding with XOR + Codecs        |
+------+---------------------------------------------------+
```


## Advanced Techniques

`encodify` offers an array of advanced encoding techniques. These include line-based encoding, various combinations of compression, and XOR encryption. For in-depth guidance on these techniques, refer to the module's extensive documentation.

## Examples

Explore some advanced examples showcasing the versatility of `encodify`:

```python
from encodify import Encodify

# Create an instance of Encodify
encoder = Encodify()

# Example 1: Encoding with m2 method
code_to_encode = "for i in range(5):\n    print(f'Number: {i}')"
encoded_code_m2 = encoder.m2(code_to_encode)

# Example 2: Encoding with l1 method
line_based_code = "print('Hello, World!')"
encoded_line_based_code = encoder.l1(line_based_code, 3)

# Example 3: Generating a random payload
random_payload = encoder.random_payload("print('Hello, World!')", 2)

# Example 4: Generating a payload with a specific encoding method (m11)
chosen_encoding_method = 11
payload_m11 = encoder.gen_payload(chosen_encoding_method, "print('Hello, World!')")

# Example 5: Customizing output with options
options = {
    "replace_strings": {"print": "display"},
    "prepend_code": "import datetime\n",
    "append_code": "\nprint(f'Execution Time: {datetime.datetime.now()}')"
}
customized_payload = encoder.gen_payload(1, "print('Hello, World!')", options=options)

```

## Best Practices and Considerations

1. **Use Responsibly**: This module is primarily intended for educational purposes. Use it responsibly and within the boundaries of applicable laws and ethical guidelines.

2. **Testing and Verification**: Always test the encoded code to ensure it functions as expected.

3. **Documentation**: Document the encoding method used and keep a record for future reference.

**Repository Views** ![Views](https://profile-counter.glitch.me/encodify/count.svg)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

