import gdown

# URL file mediafire
url = "https://download943.mediafire.com/nh5t6tlf0gugYxrHe76Ut2VzT-KbQh4Hu4TbxAkGm-aTLe8EonNdGZWlbAP3JASL8ysiQBXQ0ChvXx5EqiNN6Ef1A-jqteF7IjPUCzMaE16PzXtF0murHsOIj4GKhKWUZrmHTgCULp9GTM1_fsUyr-2avFHSYrO6IUipb2DPSirS5Ao/f4x3oz2w0aphghq/WINDOWS7HOMEBASIC64-EN.7z"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win10.zip"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
