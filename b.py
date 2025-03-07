import gdown

# URL file media fire
url = "https://www.mediafire.com/file/f4x3oz2w0aphghq/WINDOWS7HOMEBASIC64-EN.7z/file?dkey=hcrl3wmo98p&r=1923"

# Đường dẫn lưu file sau khi tải
output = "/mnt/WINDOWS7HOMEBASIC64-EN.7z"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
