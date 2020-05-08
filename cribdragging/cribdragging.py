

class bcolors:
    ENCRYPTED = '\033[91m'
    DECRYPTED = '\033[92m'
    ENDC = '\033[0m'

OTP = ''
msgs = []
decrypted_msgs = []

def print_all():
    for i in range(len(msgs)):
        print('Message #{}: '.format(i), end = '') 
        print('{}{}{}'.format(bcolors.DECRYPTED, decrypted_msgs[i], bcolors.ENDC), end = '') 
        print('{}{}{}'.format(bcolors.ENCRYPTED, msgs[i], bcolors.ENDC))

def get_OTP(secret, msg):
    n_secret = ord(secret.lower()) - ord('a')
    n_msg = ord(msg.lower()) - ord('a')
    letter = (n_secret - n_msg)
    if letter < 0:
        letter = letter + 26
    return str(chr(letter + ord('a') - 1))

def get_real_letter(secret, key):
    n_secret = ord(secret.lower()) - ord('a')
    n_key = ord(key.lower()) - ord('a')
    letter = (n_secret - n_key)
    if letter < 0:
        letter = letter + 26
    if (secret.islower()):
        letter = letter + ord('a') - 1
    else:
        letter = letter + ord('A') - 1
    return chr(letter)

def decode(next_letters, msgs, n_msg, OTP):
    for letter in next_letters:
        key = get_OTP(msgs[n_msg][0], letter)
        for n in range(len(msgs)):
            if (msgs[n][0]):
                decrypted_msgs[n] = decrypted_msgs[n] + get_real_letter(msgs[n][0], key) 
                msgs[n] = msgs[n][1:]
        OTP = OTP + key
    return OTP

n_msgs = int(input("How many messages? "))

for i in range(n_msgs):
    msgs.append(input())
    decrypted_msgs.append('')
secret_length = len(msgs[0])
while len(OTP) < secret_length:
    print(OTP)
    print_all()
    next_message = int(input("Select next message: "))
    next_letters = input("Enter the next letters in the message: ")
    OTP = decode(next_letters, msgs, next_message, OTP)