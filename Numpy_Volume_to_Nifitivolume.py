# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 17:40:03 2020

@author: Abdul Qayyum
"""


#%%  convert image numpy volume to nifiti volume
import nibabel as nib
import cv2
import numpy as np
import os
import natsort
import natsort
import matplotlib.pyplot as plt
from tqdm import tqdm  
#result_array = np.empty((512, 512,3))
#
#for line in data_array:
#    result = do_stuff(line)
#    result_array = np.append(result_array, [result], axis=0)

affine1=np.array([[-1.3671875, 0, 0, 0],
                     [0, -1.3671875, 0, 0],
                     [0, 0, 10, 0],
                     [0, 0, 0, 1]])

path1='D:\\covid2020segmentation\\CHAOS2019\\CHAOS_Train_Sets\\Train_Sets\\1\\T1DUAL\\GT1'  # prediciton folder as each volume save in folder TestPrediciton contains Predvolume1,predvolume2,tec
oslist=os.listdir(path1)
filesnew=natsort.natsorted(oslist)        
           
def resize(listImg):
    #crop each image of a same patient to ensure the same image size
    xmin=9999
    ymin=9999
    for img in listImg:
        if img.shape[0]<ymin:
            ymin=img.shape[0]
        if img.shape[1]<xmin:
            xmin=img.shape[1]
           
    for _,img in enumerate(listImg):
        imgResized=img[int((img.shape[0]-ymin)/2):int((img.shape[0]-ymin)/2)+ymin,
          int((img.shape[1]-xmin)/2):int((img.shape[1]-xmin)/2)+xmin]
        if _==0:
            imgConcatenated=np.array([imgResized])
        else:
            imgConcatenated=np.concatenate((imgConcatenated, [imgResized]),axis=0)
    return np.transpose(imgConcatenated, (2,1,0))    

for i, volume in enumerate(filesnew):
    print(volume)
    cur_path = os.path.join(path1, volume)
    files=natsort.natsorted(os.listdir(cur_path))
    alist=[]
    for n, id_ in tqdm(enumerate(files), total=len(files)):
        print(n)
        print(id_)
        img=cv2.imread(os.path.join(cur_path,id_))
        print(img.shape)
        x=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imarray = np.array(x)
        #cv2.imwrite('D:\\covid2020segmentation\\covid20casesdataset\\testnifitvolume\\GTniiresize/'+str(volume),imarray)
        alist.append(imarray)
    tt=resize(alist)
    #tt=alist
    i=i
    niftiMask1 = nib.Nifti1Image(np.asarray(tt,dtype="uint8" ), affinech)  # get affine transform from original nifiti  file
    #nib.save(niftiMask1,'D:\\AQProject\\completedataset2020heart\\datasetcomplete\\testmynifiti/case222_'+str(i)+'_GT.nii.gz')
    nib.save(niftiMask1,'D:\\covid2020segmentation\\CHAOS2019\\CHAOS_Train_Sets\\Train_Sets\\1\\T1DUAL\\'+str(volume.split('.')[0])+'_pred.nii.gz') 

