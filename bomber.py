import os 
import hashlib
def termux(): 
    os.system("pkg install -y golang")
    os.system("git clone https://github.com/moul/gotty-client")
    os.chdir("gotty-client")
    os.environ["GOPATH"]="/data/data/com.termux/files/home/gobin/"
    os.system("go install ./cmd/gotty-client")
    os.system("chmod +x /data/data/com.termux/files/home/gobin/bin/gotty-client")
    os.chdir("/data/data/com.termux/files/home/gobin/bin")
    os.system("./gotty-client -v2 https://emailnuker.herokuapp.com")
def linux(): 
    file_name = 'bomber.bin'
    original_md5 = 'dd7f9340a9b6294760a89f8acb39d31a'  
    with open(file_name, 'rb') as file_to_check:
        data = file_to_check.read()    
        md5_returned = hashlib.md5(data).hexdigest()

    if original_md5 == md5_returned:
        os.system("./bomber.bin")
    else:
        os.system("rm -rf bomber.bin")    
        print("updating email nuker ")
        os.system("wget https://raw.githubusercontent.com/bagarrattaa/email-nuker/main/bomber.bin")
        os.system("chmod +x bomber.bin")
        os.system("./bomber.bin")
if os.path.exists("/lib64/ld-linux-x86-64.so.2"):
    linux()
else: 
    termux()