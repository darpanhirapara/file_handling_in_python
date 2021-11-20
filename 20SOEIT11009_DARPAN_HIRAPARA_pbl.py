#import modules
import os
import collections

#listing file types
image_formats = ["jpg","png","jpeg","gif","webp","tiff","psd","eps","raw","bmp"]
audio_formats =["mp3","wav","aac","dsd"]
video_formats = ["mp4","avi","webm","mkv","mov"]
docs_formats = ["ai","pdf","txt","ppt","doc","docx","xls","html","htm","odt","pptx","xslx","py","ipynb","c","zip"]
application =["exe"]


#path=input(r'enter source path :')
src=input(r'enter source path :')
Dest_path = input(r'enter destination path : ')
full_path = os.path.join(Dest_path,src)


#create directories based on file extention

Dest_dirs = ["music","videos","documents","others","images","softwere"]

for d in Dest_dirs:
       dir_path = os.path.join(Dest_path,d)
       if not os.path.isdir(dir_path):
              os.mkdir(dir_path)

#map files based on extention
full_path = os.path.join(Dest_path,src)
file_mapping = collections.defaultdict(list)
files_list =os.listdir(full_path)

#print(file_mapping)
#print(files_list)

for file_name in files_list:
       if file_name[0] !='.':
          ext = file_name.split('.')[1]
          file_mapping[ext].append(file_name)
          #print(file_mapping)

#move all files to targeted directory
for f_ext,f_list in file_mapping.items():
       if f_ext in image_formats:
           for file in f_list:
                  os.rename(os.path.join(full_path,file),os.path.join(Dest_path,"images",file))
       elif f_ext in video_formats:
           for file in f_list:
                  os.rename(os.path.join(full_path,file),os.path.join(Dest_path,"videos",file))
       elif f_ext in docs_formats:
               for file in f_list:
                  os.rename(os.path.join(full_path,file),os.path.join(Dest_path,"documents",file))
       elif f_ext in audio_formats:
               for file in f_list:
                  os.rename(os.path.join(full_path,file),os.path.join(Dest_path,"music",file))
       elif f_ext in application:
               for file in f_list:
                  os.rename(os.path.join(full_path,file),os.path.join(Dest_path,"softweres",file))
       else :
              for file in f_list:
                  os.rename(os.path.join(full_path,file),os.path.join(Dest_path,"others",file))
print('Sucessfull \U0001F600')
