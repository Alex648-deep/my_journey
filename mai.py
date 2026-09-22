alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']

is_on=True

while is_on:
    choice=input("what do you want to do encrypt/decrypt:")
    message = input("Enter the message you want to encrypt:")
    shift = int(input("Enter the shift:"))
    shift=shift%26
    calculated = len(message)

    if choice =="encrypt":
        encrypt_message = []
        for num in range(0,calculated):
            position=alphabet.index(message[num])+1
            new_position = position + shift
            new_letter=alphabet[new_position]
            encrypt_message.append(new_letter)

        print(encrypt_message)
    elif choice=="decrypt":
        decrypt_message = []
        for num in range(0,calculated):
            position=alphabet.index(message[num])-1
            new_position = position - shift
            new_letter=alphabet[new_position]
            decrypt_message.append(new_letter)

        print(decrypt_message)
    else:
        print("invalid choice")

