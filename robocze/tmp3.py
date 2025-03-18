import os
import filedate

f='D:\\Python\\26_Rozpoznawanie_4\\x.mp4'



t=os.path.getctime(f)




filedate.File(f).set(
    created = t,
    modified = t,
    accessed = t)