import os,shutil
cur_path=os.path.dirname(__file__) # 取得目前路徑
print('==============================')
print(cur_path+'\\')
print('==============================')
# destfile= cur_path + "\\" + "newfile.py"
shutil.copy("shutil.py","newfile.py" )  # 檔案複製
shutil.copyfile("shutil.py","F:\\new.py" )  # 檔案複製