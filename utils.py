# Tanglish comments for clarity

def dna_mutate_key(key: str) -> str:
    """
    DNA mutation maadhiri key evolve aagum.
    Example: reverse + append + shuffle
    """
    return key[::-1] + "G"  # simple mutation demo

def dna_encrypt(message: str, key: str = "ATCG") -> (str, str):
    """
    Encrypt message using evolving DNA key
    """
    new_key = dna_mutate_key(key)
    encrypted = "".join(chr(ord(c) ^ ord(new_key[i % len(new_key)])) for i, c in enumerate(message))
    return encrypted, new_key

def dna_decrypt(encrypted: str, key: str = "ATCG") -> str:
    """
    Decrypt message using evolving DNA key
    """
    new_key = dna_mutate_key(key)
    decrypted = "".join(chr(ord(c) ^ ord(new_key[i % len(new_key)])) for i, c in enumerate(encrypted))
    return decrypted
