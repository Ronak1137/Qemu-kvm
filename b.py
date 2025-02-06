import gdown

# URL file mediafire
url = "https://download943.mediafire.com/xpkyxngjtj9gijobwTVRvbwV4W5DaRREADmXRPS0OEsHYSXbDcH0TlM3KcyhEv035jby46tYbihLWhnWeb9W207iuPNvdd4oyIdwZLvxUiFtWkmc23-QcCunM-2LxD7-0BruC5F1UyMTqS7dqK-fGFDubbIhArBj8hyJG61pCdqFun4/966vnh82itl7t4u/win11.zip"

# Đường dẫn lưu file sau khi tải
output = "/mnt/win11.zip.7z"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
