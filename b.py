import gdown

# URL file mediafire
url = "https://www.mediafire.com/file/do27y6t7m2ml0yz/WINDOWS7HOMEBASIC64-EN.zip/file?dkey=wst1rawlbbz&r=951"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win10.zip"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
