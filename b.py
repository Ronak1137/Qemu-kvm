import gdown

# URL file mediafire
url = "https://download943.mediafire.com/mgxncmul390gi0IfavgOlGGNFYdH-ulAW88zelP6h3FqDV4KjfvrI3j6x8oIPrXRLnpklljchritUAVt7odFFMB7XNqse1za489zHfbVsZVJ2lMe6rRIo9cLhY4g0B3c6ooeazqxo_XSYVrA9Kf2sGKB02ZFFJD7Ti4vamN26_MGg1I/966vnh82itl7t4u/win11.zip"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win11.zip"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
