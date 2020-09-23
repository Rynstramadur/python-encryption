# Python Encryption
## Varied-length randomized binary encryption software running in Python


### Instructions
1. Load and run main.py.
2. Enter seed data. This needs to contain only 0-9 and/or lowercase a-z. (The software utilizes base 36 to interpret seeds.)
3. Enter task: 'encrypt' or 'decrypt'
    1. **Encrypt:**
        1. Enter message to encrypt. This needs to contain only 0-9, lowercase a-z, and spaces.
        2. You get a short decimal checksum and a longer hex string. 
        3. Type 'exit' to return to the main menu.
    2. **Decrypt:**
        1. Enter hex string to decrypt.
        2. Enter decimal checksum.
        3. You get the decrypted message. (If, and only if, the seed you are using is the same seed that the person who encrypted the message used.)
        4. Type 'exit' to return to the main menu.


### How It Works.
1. Take a seed value, generate pseudorandom data, use that to set up the varied-length binary array *'morsearray'* (Under a specific set of conditions that should not be changed unless you understand the code.)
2. Asks to encrypt or decrypt.
    1. **Encrypt:**
        1. Break the input string into a list of the component letters/numbers.
        2. Create a list of the *morsearray* 'characters' with equivalent indexes to the characters in the forementioned list.
        3. Concatenate the second list into a string, items separated by '000'. **The length of this string is the decimal checksum.**
        4. Pad the end of the string so that the length is evenly divisible by eight.
        5. Separate the string into a list of 8 bit fixed-length binary bytes.
        6. Convert each byte to hex.
        7. Concatenate the hex bytes into a string. **This string is your encrypted message.**
    2. **Decrypt:**
        1. Split the input string into its component bytes.
        2. Convert each hex byte to binary.
        3. Concatenate the binary bytes into a string.
        4. Truncate the string at the length provided by the checksum.
        5. Split the string into a list. (at '000')
        6. Create a list of characters with equivalent indexes to the *morsearray* 'characters' in the forementioned list.
        7. Concatenate the list of characters into a string. **This string is your decrypted message.**
