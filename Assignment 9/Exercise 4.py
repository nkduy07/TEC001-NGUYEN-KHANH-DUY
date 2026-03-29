def caesar_cipher(input_file, shift, direction):
    file_in = open(input_file, 'r')
    content = file_in.read()
    file_in.close()

    for char in content:
        if char.isalpha():
            if char.isupper():
                base = 65
            else:
                base = 97

            if direction == 'right':
                new_ascii = (ord(char) - base + shift) % 26 + base
            else:
                new_ascii = (ord(char) - base - shift) % 26 + base

            result = chr(new_ascii)
        else:
            result = char

    file_out = open("ciphertext.txt", "w")
    file_out.write(result)
    file_out.close()

#Test
caesar_cipher("1", 2, 'right')
