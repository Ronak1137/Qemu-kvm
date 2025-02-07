import gdown

# URL file google drive
url = "https://drive.usercontent.google.com/download?id=11reY6uzf0BdTLLbCj_ecs0qDxWFaLTEx&authuser=0"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win10.zip"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
