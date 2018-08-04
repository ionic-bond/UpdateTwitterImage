import os

def RenameImg(dir_path, file_name):
    after_point = file_name.split('.')[-1]
    after__ = after_point.split('_')[-1]
    if after__ == "orig":
        old_path = os.path.join(dir_path, file_name)
        new_path = os.path.join(dir_path, file_name[:-5])
        if os.path.exists(new_path):
            print new_path, "already exists."
            return
        os.rename(old_path, new_path)
        print new_path

def ScanDir(dir_path):
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isdir(file_path):
            ScanDir(file_path)
        else:
            RenameImg(dir_path, file_name)


if __name__ == '__main__':
    ScanDir(r'F:\Image')
    os.system("pause")
