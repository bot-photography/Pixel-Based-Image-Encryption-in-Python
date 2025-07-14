from PIL import Image

def encrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        if img.mode != "RGB":
            img = img.convert("RGB")

        pixels = img.load()
        width, height = img.size

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[x, y] = (r, g, b)

        img.save(output_path)
        print(f"[✔] Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"[!] Encryption Error: {e}")

def decrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        if img.mode != "RGB":
            img = img.convert("RGB")

        pixels = img.load()
        width, height = img.size

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[x, y] = (r, g, b)

        img.save(output_path)
        print(f"[✔] Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"[!] Decryption Error: {e}")