import os

folder = r"D:\năm 4\Cưới\images\album"   # đổi đường dẫn thư mục của bạn

files = sorted(f for f in os.listdir(folder) if f.lower().endswith(".jpg"))

for i, file in enumerate(files, 1):
    old = os.path.join(folder, file)
    new = os.path.join(folder, f"{i}.jpg")
    os.rename(old, new)
