import os
import sys
import urllib

num = 0
orig = 0
large = 0
default = 0
error = 0

def UpdateImg(dir_path, file_name):
    suf=file_name.split('.')[0]
    if len(suf)==15:
        path = os.path.join(dir_path, file_name)
        path = "G" + path[1:]
        if os.path.exists(path):
            return
        global num
        global orig
        global large
        global default
        global error
        num += 1
        print num, path

        try:
            url = r"https://pbs.twimg.com/media/" + file_name + r":orig"
            data = urllib.urlopen(url).read()
            if len(data)==0:
                url = r"https://pbs.twimg.com/media/" + file_name + r":large"
                data = urllib.urlopen(url).read()
                if len(data)==0:
                    url = r"https://pbs.twimg.com/media/" + file_name
                    data = urllib.urlopen(url).read()
                    if len(data)==0:
                        error += 1
                        print "Error!"
                        f = file(r"G:\log.txt", "a")
                        print >> f, os.path.join(dir_path, file_name)
                        return
                    else:
                        default += 1
                else:
                    large += 1
            else:
                orig += 1
        except IOError:
            f = file(r"G:\error.txt", "a")
            print >> f, "IOError: " + path
            print "IOError!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print path
            return

        tmp_dir_path = "G" + dir_path[1:]
        if not os.path.exists(tmp_dir_path):
            os.makedirs(tmp_dir_path)
        f = file(path, "wb")  
        f.write(data)  
        f.close()
        print "Succese download from", url

def ScanDir(dir_path):
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isdir(file_path):
            ScanDir(file_path)
        else:
            UpdateImg(dir_path, file_name)


if __name__ == '__main__':
    ScanDir(r'F:\Image')
    print "sum: ", num
    print "orig: ", orig
    print "large: ", large
    print "default: ", default
    print "error: ", error
