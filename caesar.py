alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

# def encrypt(original_text,shift_amount):
#    cipher=""
#    for letter in original_text:
#
#        shift_num=alphabet.index(letter)+shift_amount
#        shift_num%=len(alphabet)
#        cipher+=alphabet[shift_num]
#    print(cipher)
# encrypt(original_text=text ,shift_amount=shift)

# def decrypt(original_text,shift_amount):
#     ciphertext=""
#     for letter in original_text:
#         shift_num=alphabet.index(letter)-shift_amount
#         shift_num %= len(alphabet)
#         ciphertext+=alphabet[shift_num]
#     print(ciphertext)
# decrypt(original_text=text ,shift_amount=shift)

def caesar(original_text,shift_amount,encode_decode):
    ciphertext = ""
    if encode_decode == "decode":
        shift_amount *= -1
    for letter in original_text:

        shift_num=alphabet.index(letter)+shift_amount
        shift_num %= len(alphabet)
        ciphertext+=alphabet[shift_num]
    print(ciphertext)
caesar(original_text=text ,shift_amount=shift,encode_decode=direction)
