# Criptografia do Voto
def encrypt_vote(vote, public_key):
    cipher = AES.new(public_key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(vote.encode(), AES.block_size))
    iv = cipher.iv
    return iv + ct_bytes

def decrypt_vote(encrypted_vote, private_key):
    iv = encrypted_vote[:16]
    ct = encrypted_vote[16:]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()