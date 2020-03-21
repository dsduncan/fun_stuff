import glob 
import os
from PIL import Image
import shutil

src_pth = os.path.join(
    os.path.expanduser('~'),
   'Appdata/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/')

des_pth = 'E:/Pictures/Backgrounds'
extn = '.jpg'

src_pth_list = glob.glob(src_pth + '*')
src_name_list = [os.path.split(f)[1] for f in src_pth_list]

des_pth_list = [os.path.join(des_pth, f + extn) for f in src_name_list]\

dims = [Image.open(f).size for f in src_pth_list]

for src, des, dim in zip(src_pth_list, des_pth_list, dims):
    if dim[0] > dim[1]:
        shutil.copy2(src, des)
