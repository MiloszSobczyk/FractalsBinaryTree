import os

def delete_gifs_and_pngs(path):
    if not os.path.exists(path):
        return
    
    for filename in os.listdir(path):
        if filename.endswith(".gif") or filename.endswith(".png"):
            file_path = os.path.join(path, filename)
            os.remove(file_path)

delete_gifs_and_pngs('./gifs/')   