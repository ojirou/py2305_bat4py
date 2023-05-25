import subprocess
def main():
    pyfile= input('バッチファイル名（拡張子除く）>> ')  
    path=r'C:\Users\user\anaconda3\Scripts\xxxxx.bat'
    with open(path) as f:
        s=f.read()
#        print(type(s))
#        print(s)    
    s=s.replace('xxxxx', pyfile)
    path_w='C:\\Users\\user\\anaconda3\\Scripts\\'+pyfile+'.bat'
    with open(path_w, mode='w') as f:
        f.write(s)
#    with open(path_w) as f:
#        print(f.read())
#    subprocess.Popen(["notepad", path_w])
if __name__ == "__main__":
    main()