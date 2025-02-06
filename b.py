import gdown

# URL file mediafire
url = "https://download943.mediafire.com/w0tkbcxmy2pg08PGmCN6PSK6vchFwvJloXKbfIaQ2tgXseZ-5aw-wWI1pITNpFqI9dKnrz8mRtOz_tEqBATmRWi1-lwNBpffytrGdkadqIya9BmFBkrqs-yvtc0yStcrT2qgCcqHZu2ydeMs1JT8jfnJW_-75xhXRA9aTYjns930yWE/do27y6t7m2ml0yz/WINDOWS7HOMEBASIC64-EN.zip"

# Đường dẫn lưu file sau khi tải
output = "/mnt/WINDOWS7HOMEBASIC64-EN.zip"  # Đổi tên file tùy ý

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
