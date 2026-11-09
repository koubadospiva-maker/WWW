import hashlib
import urllib.parse

email = input("Zadejte e-mail: ")

# Normalizace a převod na bajty
cisty_email = email.strip().lower().encode("utf-8")
hash_sha256 = hashlib.sha256(cisty_email).hexdigest()

parametry = urllib.parse.urlencode({"s": 200, "d": "identicon"})
gravatar_url = f"https://www.gravatar.com/avatar/{hash_sha256}?{parametry}"

print("\n--- VÝSLEDEK ---")
print(f"Normalizovaný e-mail: {email.strip().lower()}")
print(f"SHA-256 hash (64 znaků): {hash_sha256}")
print(f"Výsledná Gravatar URL:\n{gravatar_url}")