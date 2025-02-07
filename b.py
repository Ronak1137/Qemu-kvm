import gdown

# URL file google drive
url = "https://download943.mediafire.com/3tde0tapzfcgmAHEBbtD-ooY9FbowyZgurwpQ9nuORnL7b7bgOBc5vhG-zD9mQ1C9cQNcjIgkYV5mAMAu_ym2A47c5A-wzM85KiowfR5V_FCplxyZ-CKP6tTUdPP7520DcdXvZ5DJlGuAQE80IwF_83piowZuJpu5nPtHrTchZVPn68/f4x3oz2w0aphghq/WINDOWS7HOMwzM85KiowfR5V_FCplxyZ-CKP6tTUdPP7520DcdXvZ5DJlGuAQE80IwF_83piowZuJpu5nPtHrTchZVPn68/f4x3oz2w0aphghq/WINDOWS7HOMEBASIC6w0aphghq/WINDOWS7HOMwzM85KiowfR5V_FCplxyZ-CKP6tTUdPP7520DcdXvZ5DJlGuAQE80IwF_83piowZuJpu5nPtHrTchZVPn68/f4x3oz2w0aphghq/WINDOWS7HOMEBASIC64-EN.7z"EBASIC64-EN.7z4-EN.7z"EBASIC64-EN.7z"

# Đường dẫn lưu file sau khi tải
output = "/mnt/WINDOWS7HOMEBASIC64-EN.7z"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
