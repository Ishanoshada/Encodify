"""
encodify - A module providing various encoding methods for Python code.
Author: Ishan Oshada

"""

import random
import string
import subprocess
import os
import python_minifier
import marshal
import base64
import gzip
import lzma
import zlib

class Encodify:
    """
    This class provides various encoding methods for Python code. It includes methods for encoding using compression, 
    base64 encoding, and xor encryption. Additionally, it offers options for customizing the encoded output.

    Methods:
        - m1 to m11: Different encoding techniques utilizing combinations of compression and base64 encoding.
        - m20: Encodes code after minifying it with python_minifier.
        - l1 and l2: Line-based encoding techniques with multiple iterations.
        - line_encoded_23 to line_encoded_30: Line-based encoding with variations of base64 encoding and compression.

    Utility Methods:
        - xor_encrypt: XOR encryption method.

    Random Payload Generation:
        - random_payload: Randomly selects an encoding function and applies it to provided data.
        - gen_payload: Generates a payload based on a specific encoding choice.

    Additional Information:
        - This code also includes imports for various libraries used in the encoding methods.

    Note: Please ensure to handle exceptions appropriately when using encoding functions.
    """
    
    
    def __init__(self):
        pass

    def m1(self, code):
        try:
            code = code.encode()
        except:
            code = code
        en = gzip.compress(marshal.dumps(compile(code, "_name_", "exec")))
        output = "import base64,marshal,binascii,gzip,zlib\n"
        output += f"#Encoded by encodify\n"
        output += "try:\n"
        output += f"\texec(marshal.loads(gzip.decompress({en})))\n"
        output += "except Exception as b:\n\tprint(f'Error by {b} ')"
        return output

    def m2(self, data):
        en = lzma.compress(base64.b64encode(marshal.dumps(compile(data, "_name_", "exec"))))
        return f"import marshal,base64,lzma\nexec(marshal.loads(base64.b64decode(lzma.decompress({en}))))"

    def m3(self, data):
        en = lzma.compress(base64.b85encode(marshal.dumps(compile(data, "_name_", "exec"))))
        return f"import marshal,base64,lzma\nexec(marshal.loads(base64.b85decode(lzma.decompress({en}))))"

    def m4(self, data):
        en = lzma.compress(marshal.dumps(compile(data, "_name_", "exec")))
        output = f"#Encoded by encodify\n"
        output += "import binascii,lzma,base64,marshal,gzip,zlib\n"
        output += f"\ntry:\n\texec(marshal.loads(lzma.decompress({en})))\n\n\nexcept Exception as b:\n\n\t"+"print(f'\\n\\n\\tError to : {b}\\n\\n ')"
        return output

    def m5(self, data):
        en = base64.b64encode(lzma.compress(marshal.dumps(compile(data, "_name_", "exec"))))
        return f"import marshal,lzma,base64\nexec(marshal.loads(lzma.decompress(base64.b64decode({en}))))"

    def m6(self, data):
        en = lzma.compress(zlib.compress(marshal.dumps(compile(data, "_name_", "exec"))))
        return f"import marshal,zlib,lzma\nexec(marshal.loads(zlib.decompress(lzma.decompress({en}))))"

    def m7(self, data):
        en = lzma.compress(gzip.compress(marshal.dumps(compile(data, "_name_", "exec"))))
        return f"import marshal,gzip,lzma\nexec(marshal.loads(gzip.decompress(lzma.decompress({en}))))"

    def m8(self, data):
        en = lzma.compress(marshal.dumps(compile(data, "_name_", "exec")))
        return f"import marshal,lzma\nexec(marshal.loads(lzma.decompress({en})))"

    def m9(self, code):
        en = base64.b64encode(gzip.compress(marshal.dumps(compile(code, "_name_", "exec"))))
        output = f"#ENCODED BY encodify \n#you can try this decode\n"
        output += "import marshal,base64,gzip,zlib,bz2,lzma\n"
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"
        return output

    def m10(self, code):
        code1 = compile(code, "_name_", 'exec')
        en = base64.b64encode(gzip.compress(marshal.dumps(code1)))
        return f"import marshal,base64,gzip,lzma;exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"

    def m11(self, code):
        try:
            code = code.encode()
        except:
            code = code
        finally:
            en = base64.b64encode(gzip.compress(marshal.dumps(compile(code, "_name_", "exec"))))
            output = f"#ENCODED BY encodify \n#you can try this decode\n"
            output += "import marshal,base64,gzip,zlib,bz2,lzma\n"
            output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"
        return output

    def m20(self, code):
        data = python_minifier.minify(code).encode()
        en = base64.b64encode(gzip.compress(marshal.dumps(compile(code, "_name_", "exec"))))
        output = "#ENCODED BY encodify\n"
        output += f"#you can try this decode\n"
        output += "import marshal,base64,gzip,zlib,bz2,lzma\n"
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"
        return output

    

    def l1(self, data, line):
        output = "import marshal,base64,lzma,gzip,zlib,binascii\n"
        output += "#https://github.com/Ishanoshada/encodify\n"
        for i in range(line):
            if int(line/2) == i:
                en = gzip.compress(base64.b85encode(marshal.dumps(data)))
                output += f"exec(marshal.loads(base64.b85decode(gzip.decompress({en}))));"
            else:
                da = f"#{base64.b85encode(lzma.compress(data.encode())).decode()}"
                en = gzip.compress(base64.b85encode(marshal.dumps(da)))
                output += f"exec(marshal.loads(base64.b85decode(gzip.decompress({en}))));"
        return output

    def l2(self, data, line):
        output = "import marshal,base64,lzma,gzip,zlib,binascii\n"
        output += "#https://github.com/Ishanoshada/encodify\n"
        for i in range(line):
            if int(line/2) == i:
                en = lzma.compress(gzip.compress(base64.b85encode(marshal.dumps(data))))
                output += f"exec(marshal.loads(base64.b85decode(gzip.decompress(lzma.decompress({en})))));"
            else:
                da = f"#{base64.b85encode(lzma.compress(data.encode())).decode()}"
                en = lzma.compress(gzip.compress(base64.b85encode(marshal.dumps(da))))
                output += f"exec(marshal.loads(base64.b85decode(gzip.decompress(lzma.decompress({en})))));"
        return output

    def line_encoded_23(self, code, n):
        try:
            code = code.encode()
        except:
            code = code
        output = f"#ENCODE BY encodify \n#you can try this decode\n"
        output += "#https://github.com/Ishanoshada/encodify\n"
        output += "import marshal,base64,gzip,zlib,bz2\n"
        for i in range(n):
            en = base64.b64encode(gzip.compress(marshal.dumps(f"#{bz2.compress(base64.b64encode(code))}")))
            output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
            if int(i/2) == i:
                en = base64.b64encode(gzip.compress(marshal.dumps(code)))
                output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
        return output

    def line_encoded_24(self, code, n):
        try:
            code = code.encode()
        except:
            code = code
        output = f"#ENCODED BY encodify \n#you can try this decode\n"
        output += "#https://github.com/Ishanoshada/encodify\n"
        output += "import marshal,base64,gzip,zlib,bz2,lzma\n"
        for i in range(n):
            en = base64.b64encode(gzip.compress(marshal.dumps(compile(f"#{bz2.compress(base64.b64encode(marshal.dumps(code)))}", "_name_", "exec"))))
            output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
            if int(i/2) == i:
                en = base64.b64encode(gzip.compress(marshal.dumps(compile(code, "_name_", "exec"))))
                output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
        return output

    def line_encoded_25(self, code, n):
        _name_ = "encodify"
        try:
            code = code.encode()
        except:
            code = code
        output = f"#ENCODED BY {_name_} \n#you can try this decode\n"
        output += "#https://github.com/Ishanoshada/encodify\n"
        output += "import marshal, base64,lzma\n"
        for i in range(n):
            en = base64.a85encode(marshal.dumps(compile(f"#{base64.a85encode(marshal.dumps(code)).decode()}", "_name_", 'exec'))).decode()
            output += f'exec(marshal.loads(base64.a85decode("""{en}""")))\n'
            if int(i / 2) == i:
                en = base64.a85encode(marshal.dumps(compile(code, "_name_", 'exec'))).decode()
                output += f'exec(marshal.loads(base64.a85decode("""{en}""")))\n'
        return output

    def line_encoded_26(self, code, n):
        _name_ = "encodify"
        try:
            code = code.encode()
        except:
            code = code
        output = f"#ENCODED BY {_name_} \n#you can try this decode\n"
        output += "#https://github.com/Ishanoshada/encodify\n"
        output += "import marshal, base64, codecs\n"
        for i in range(n):
            en = base64.b64encode(marshal.dumps(compile(f"#codecs.encode({code}, 'rot_13').decode()", "_name_", 'exec'))).decode()
            output += f'exec(marshal.loads(base64.b64decode("""{en}""")))\n'
            if int(i / 2) == i:
                en = base64.b64encode(marshal.dumps(compile(code, "_name_", 'exec'))).decode()
                output += f'exec(marshal.loads(base64.b64decode("""{en}""")))\n'
        return output

    def xor_encrypt(self, data, key):
        key = key.encode()
        encrypted = bytearray()
        for i in range(len(data)):
            encrypted.append(data[i] ^ key[i % len(key)])
        return encrypted

    def line_encoded_27(self, code, n):
        try:
            code = code.encode()
        except:
            code = code
        output = f"#ENCODED BY encodify \n#you can try this decode\n"
        output += "#https://github.com/Ishanoshada/encodify\n"
        output += "import marshal, base64\n"
        for i in range(n):
            en = base64.b64encode(self.xor_encrypt(marshal.dumps(compile(f"#{base64.b64encode(self.xor_encrypt(marshal.dumps(code), 'ishan')).decode()}", "_name_", 'exec')), 'ishan')).decode()
            output += f'exec(marshal.loads(self.xor_encrypt(base64.b64decode("""{en}"""), "ishan")))\n'
            if int(i / 2) == i:
                en = base64.b64encode(self.xor_encrypt(marshal.dumps(compile(code, "_name_", 'exec')), 'ishan')).decode()
                output += f'exec(marshal.loads(self.xor_encrypt(base64.b64decode("""{en}"""), "ishan")))\n'
        return output

    def line_encoded_28(self, code, n):
        try:
            code = code.encode()
        except:
            code = code
        output = f"#ENCODED BY encodify \n#you can try this decode\n"
        output += "#https://github.com/Ishanoshada/encodify\n"
        output += "import marshal, base64\n"
        for i in range(n):
            en = base64.b64encode(self.xor_encrypt(marshal.dumps(compile(f"#base64.b64encode({code}).decode()'", "_name_", 'exec')), 'ishan')).decode()
            output += f'exec(marshal.loads(self.xor_encrypt(base64.b64decode("""{en}"""), "ishan")))\n'
            if int(i / 2) == i:
                en = base64.b64encode(self.xor_encrypt(marshal.dumps(compile(code, "_name_", 'exec')), 'ishan')).decode()
                output += f'exec(marshal.loads(self.xor_encrypt(base64.b64decode("""{en}"""), "ishan")))\n'
        return output

    def line_encoded_29(self, code, n):
        try:
            code = code.encode()
        except:
            code = code
        output = f"#ENCODED BY encodify \n#you can try this decode\n"
        output += "#https://github.com/Ishanoshada/encodify\n"
        output += "import marshal, base64\n"
        for i in range(n):
            en = base64.b64encode(self.xor_encrypt(marshal.dumps(compile(f"#base64.b64decode({code})", "_name_", 'exec')), 'ishan')).decode()
            output += f'exec(marshal.loads(self.xor_encrypt(base64.b64decode("""{en}"""), "ishan")))\n'
            if int(i / 2) == i:
                en = base64.b64encode(self.xor_encrypt(marshal.dumps(compile(code, "_name_", 'exec')), 'ishan')).decode()
                output += f'exec(marshal.loads(self.xor_encrypt(base64.b64decode("""{en}"""), "ishan")))\n'
        return output

    def line_encoded_30(self, code, n):
        _name_ = "encodify"
        try:
            code = code.encode()
        except:
            code = code
        output = f"#ENCODED BY {_name_} \n#you can try this decode\n"
        output += "#https://github.com/Ishanoshada/encodify\n"
        output += "import marshal, base64, codecs\n"
        for i in range(n):
            en = base64.b64encode(self.xor_encrypt(marshal.dumps(compile(f"#codecs.encode({code}, 'rot_13').decode()'", "_name_", 'exec')), 'ishan')).decode()
            output += f'exec(marshal.loads(self.xor_encrypt(base64.b64decode("""{en}"""), "ishan")))\n'
            if int(i / 2) == i:
                en = base64.b64encode(self.xor_encrypt(marshal.dumps(compile(code, "_name_", 'exec')), 'ishan')).decode()
                output += f'exec(marshal.loads(self.xor_encrypt(base64.b64decode("""{en}"""), "ishan")))\n'
        return output
     
    def random_payload(self, data, line=1, options=None):
        """
    Randomly selects an encoding function and applies it to provided data.

    Parameters:
        data (str): The input Python code to be encoded.
        line (int): The number of lines for line-based encoding.
        options (dict, optional): Additional options for customization (default is None).

    Returns:
        str: The encoded Python code payload.
    """
        if options is None:
            options = {}

        encoding_functions = [
            self.m1, self.m2, self.m3, self.m4, self.m5,
            self.m6, self.m7, self.m8, self.m9, self.m10,
            self.m11, self.m20, self.l1, self.l2, self.line_encoded_25,
            self.line_encoded_26, self.line_encoded_27, self.line_encoded_28,
            self.line_encoded_29, self.line_encoded_30
        ]

        # Choose a random encoding function
        choice = random.choice(encoding_functions)

        if callable(choice):
            try:
              result = choice(data)
            except:
                result = choice(data,n=2)

            # Additional options for customization
            if "replace_strings" in options:
                for old_str, new_str in options["replace_strings"].items():
                    result = result.replace(old_str, new_str)

            if "prepend_code" in options:
                result = options["prepend_code"] + result

            if "append_code" in options:
                result += options["append_code"]

            return result
        else:
            return "Random encoding function choice failed."
            
     
     
    def gen_payload(self, choice, data, line=2, options=None):
     """
    Generates a payload based on a specific encoding choice.

    Parameters:
        choice (int): The encoding technique choice.
        data (str): The input Python code to be encoded.
        line (int, optional): The number of lines for line-based encoding (default is 2).
        options (dict, optional): Additional options for customization (default is None).

    Returns:
        str: The encoded Python code payload.
    """
     if options is None:
        options = {}
     encoding_functions = {
            1: self.m1,
            2: self.m2,
            3: self.m3,
            4: self.m4,
            5: self.m5,
            6: self.m6,
            7: self.m7,
            8: self.m8,
            9: self.m9,
            10: self.m10,
            11: self.m11,
            20: self.m20,
            23: self.l1,
            24: self.l2,
            25: self.line_encoded_25,
            26: self.line_encoded_26,
            27: self.line_encoded_27,
            28: self.line_encoded_28,
            29: self.line_encoded_29,
            30: self.line_encoded_30,
            # Add more encoding techniques here as needed
        }
     if choice in encoding_functions:
       try:
         result = encoding_functions[choice](data)
       except:
           result = encoding_functions[choice](data,n=2)
     else:
        return "Invalid choice. Please select a valid option."

    # Additional options for customization
     if "replace_strings" in options:
        for old_str, new_str in options["replace_strings"].items():
            result = result.replace(old_str, new_str)

     if "prepend_code" in options:
        result = options["prepend_code"] + result

     if "append_code" in options:
        result += options["append_code"]

     return result


__all__ = ['Encodify']
__author__ = "Ishan"
__package__ = "encodify"

