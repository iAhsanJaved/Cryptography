# Playfair algorithm
def encrypt(plaintext, playfair_matrix):
    """ This fuction will return Ciphertext"""

    # Converting plaintext into Uppercase letters and Removing spaces and other characters
    temp = ''
    for ch in plaintext:
        if ch.isalpha():
            temp += ch.upper()
        else:
            continue
    plaintext = temp

    # Splitting string into list of characters; Add 'X' between same character
    plaintext_char_list = []
    plaintext_char_list.append(plaintext[0])
    index = 1
    while index < len(plaintext):
        if plaintext[index] == plaintext_char_list[-1]:
            plaintext_char_list.append('X')
            index = index - 1
        else:
            plaintext_char_list.append(plaintext[index])
        index = index + 1
    # If length of string is Odd then add 'X' or 'Y' at end of string
    if len(plaintext_char_list)%2 != 0:
        if plaintext_char_list[-1] == 'X':
            plaintext_char_list.append('Y')
        else:
            plaintext_char_list.append('X')


    # Pairing
    plaintext_pairs = []
    for i in range(0, len(plaintext_char_list), 2):
        plaintext_pairs.append([plaintext_char_list[i], plaintext_char_list[i+1]])

    def findindex(searchkey, matrix):
        if searchkey == 'J' or searchkey == 'K':
            return (0, 0)
        for i in range(0, len(matrix)):
            if searchkey in matrix[i]:
                j = matrix[i].index(searchkey)
                return (i, j)


    for i, pair in enumerate(plaintext_pairs):
        first_ith, first_jth = findindex(pair[0], playfair_matrix)
        second_ith, second_jth = findindex(pair[1], playfair_matrix)

        if first_jth == second_jth:
            pair[0] = playfair_matrix[(first_ith+1)%5][first_jth]
            pair[1] = playfair_matrix[(second_ith+1)%5][second_jth]
        elif first_ith == second_ith:
            pair[0] = playfair_matrix[first_ith][(first_jth+1)%5]
            pair[1] = playfair_matrix[second_ith][(second_jth+1)%5]
        else:
            pair[0] = playfair_matrix[second_ith][first_jth]
            pair[1] = playfair_matrix[first_ith][second_jth]

    ciphertext = ''

    for pair in plaintext_pairs:
        ciphertext += pair[0]
        ciphertext += pair[1]
    return ciphertext

playfair_matrix = [
    ['J/K', 'C', 'D', 'E', 'F'],
    ['U', 'N', 'P', 'Q', 'S'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['R', 'A', 'L', 'G', 'O'],
    ['B', 'I', 'T', 'H', 'M']
]

plaintext = input('Enter the plaintext: ')

# Playfair encryption
ciphertext = encrypt(plaintext, playfair_matrix)

print('\nPlaintext: ' + plaintext)
print('Ciphertext: ' + ciphertext)