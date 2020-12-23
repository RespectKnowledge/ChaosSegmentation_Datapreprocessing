# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 17:36:54 2020

@author: moona
"""


#%%  MRI chaos images for both dula t1 and tspr and convert all images into nifiti array as a volume

import os
import numpy as np
import matplotlib.pyplot as mpplot
import matplotlib.image as mpimg
import glob
import SimpleITK as sitk

images = []
#folders = glob.glob('C:\\Users\\abdul\\Desktop\\Tutorialformha\\CHAOS_Train_Sets\\CHAOS_Train_Sets\\Train_Sets\\MR\\*\\*')
path='D:\\covid2020segmentation\\CHAOS2019\\CHAOS_Train_Sets\\Train_Sets\\MR\\'
save_path_TsprImg='D:\\covid2020segmentation\\CHAOS2019\\CHAOS_Train_Sets\\Train_Sets\\niifiles\\Tsrimagenii1\\'
save_path_Tsprmsk='D:\\covid2020segmentation\\CHAOS2019\\CHAOS_Train_Sets\\Train_Sets\\niifiles\\Tsrmasknii1\\'

save_path_Tidualmask='D:\\covid2020segmentation\\CHAOS2019\\CHAOS_Train_Sets\\Train_Sets\\niifiles\\Tidualmasknii1\\'
save_path_Tidualimgin='D:\\covid2020segmentation\\CHAOS2019\\CHAOS_Train_Sets\\Train_Sets\\niifiles\\T1dualimginnii1\\'
save_path_Tidualimgout='D:\\covid2020segmentation\\CHAOS2019\\CHAOS_Train_Sets\\Train_Sets\\niifiles\\t1dualimgoutnii1\\'

patient_pattern = os.path.join(path,'*')
patient_list = glob.glob(patient_pattern)
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
for pa in patient_list:
    patients_pattern_1 = os.path.join(pa,'T1DUAL','*','*')
    patients_pattern_2 = os.path.join(pa,'T2SPIR','*','*')
    patients_pattern_1n = os.path.join(pa,'T1DUAL','DICOM_anon','InPhase','*')
    patients_pattern_out = os.path.join(pa,'T1DUAL','DICOM_anon','OutPhase','*')
    patients_list_1 = glob.glob(patients_pattern_1)
    patients_list_2 = glob.glob(patients_pattern_2)
    patients_list_In = glob.glob(patients_pattern_1n)
    patients_list_out = glob.glob(patients_pattern_out)
    lstFilesT2SPIRIm = []  # create an empty list
    lstFilesT2SPIRmask=[]
    lstFilesT1DUALmask=[]
    lstFilesT1DUALInphase=[]
    lstFilesT1DUALOutphase=[]
    for filename in patients_list_2:
        if ".dcm" in filename.lower():  # check whether the file's pngs
            lstFilesT2SPIRIm.append(filename)
        if ".png" in filename.lower():  # check whether the file's pngs
            lstFilesT2SPIRmask.append(filename)
    for filename in patients_list_1:
        if ".png" in filename.lower():  # check whether the file's pngs
            lstFilesT1DUALmask.append(filename)
    for filename in patients_list_In:
        if ".dcm" in filename.lower():  # check whether the file's pngs
            lstFilesT1DUALInphase.append(filename) 
    for filename in patients_list_out:
        if ".dcm" in filename.lower():  # check whether the file's pngs
            lstFilesT1DUALOutphase.append(filename) 
    
    # read dcm images for T2SPIR and store as volume for each subject
    reader = sitk.ImageSeriesReader()
    reader.SetFileNames(lstFilesT2SPIRIm)
    maskct= reader.Execute()
    #save_path=os.path.join(mask_save,datadir.split('\\')[-1])
    
    new_ct_namet = 'imgtspr'+pa.split('\\')[-1]
    save_pathnew1=save_path_TsprImg+'\\'+new_ct_namet
    #save_pathnew11=os.path.join(save_pathnew1,pa.split('\\')[-1]+'.nii')
    if not os.path.exists(save_pathnew1):
        os.makedirs(save_pathnew1)
    #createFolder(save_pathnew1)
    #sitk.WriteImage(maskct,os.path.join(save_pathnew1 ,'imgtspr'+pa.split('\\')[-1]+'.nii'))
    sitk.WriteImage(maskct,os.path.join(save_pathnew1 ,'data'+'.nii'+'.gz'))
    
    # new_ct_namet =pa.split('\\')[-1]+ '.nii'
    # save_pathnew1=save_path_TsprImg+new_ct_namet
    # save_pathnew11=os.path.join(save_pathnew1,pa.split('\\')[-1])
    # createFolder(save_pathnew11)
    # sitk.WriteImage(maskct,save_pathnew11)
    
    # read png mask for T2SPIR and store as volume for each subject
    readerm1 = sitk.ImageSeriesReader()
    readerm1.SetFileNames(lstFilesT2SPIRmask)
    maskctm1= readerm1.Execute()
    ndammm1 = sitk.GetArrayFromImage(maskctm1)
    ndammm1[ndammm1==63]=1
    ndammm1[ndammm1==126]=2
    ndammm1[ndammm1==189]=3
    ndammm1[ndammm1==252]=4
    maskctm1 = sitk.GetImageFromArray(ndammm1)
    #save_path=os.path.join(mask_save,datadir.split('\\')[-1])
    
    # new_ct_namem = 'masktspr-'+pa.split('\\')[-1]
    # save_pathnew1=save_path_Tsprmsk+new_ct_namet
    # if not os.path.exists(save_pathnew1):
    #     os.makedirs(save_pathnew1)
    
    sitk.WriteImage(maskctm1,os.path.join(save_pathnew1 ,'label'+'.nii'+'.gz'))
    

# ndamm = sitk.GetArrayFromImage(maskct)  
# ndmm=ndamm[1,:,:]
# # Liver x>0 x=63 (55<<<70)
# # Right kidney - x=126 (110<<<135)
# # Left kidney - x=189 (175<<<200)
# # Spleen - x=252 (240<<<255)
# # Background Other values Other values
# ndamm[ndamm==63]=1
# ndamm[ndamm==126]=2
# ndamm[ndamm==189]=3
# ndamm[ndamm==252]=4
  
    # read png mask for T1DUAL and store as volume for each subject
    # readerm2 = sitk.ImageSeriesReader()
    # readerm2.SetFileNames(lstFilesT1DUALmask)
    # maskctm2= readerm2.Execute()
    # ndammm2 = sitk.GetArrayFromImage(maskctm2)
    # ndammm2[ndammm2==63]=1
    # ndammm2[ndammm2==126]=2
    # ndammm2[ndammm2==189]=3
    # ndammm2[ndammm2==252]=4
    
    # maskct2 = sitk.GetImageFromArray(ndammm2)
    # #save_path=os.path.join(mask_save,datadir.split('\\')[-1])
    
    # new_ct_namem = 'imginT1DUAL-'+pa.split('\\')[-1]
    # save_pathnewt1i=save_path_Tidualmask+new_ct_namem
    # if not os.path.exists(save_pathnewt1i):
    #     os.makedirs(save_pathnewt1i)
    
    # #sitk.WriteImage(maskct2,os.path.join(save_pathnew21 ,'maskT1DUAL'+pa.split('\\')[-1]+'.nii'))
    # sitk.WriteImage(maskct2,os.path.join(save_pathnewt1i ,'label'+'.nii'+'.gz'))
    
    # # new_ct_namet1m = 'maskT1DUAL-'+pa.split('\\')[-1]+ '.nii'
    # # save_pathnewt1m=save_path_Tidualmask+new_ct_namet1m
    # # sitk.WriteImage(maskct2,save_pathnewt1m)
    
    # # read dcm image for T1DUAL and store as volume for each subject for inphase
    # reader1 = sitk.ImageSeriesReader()
    # reader1.SetFileNames(lstFilesT1DUALInphase)
    # maskctp= reader1.Execute()
    # #save_path=os.path.join(mask_save,datadir.split('\\')[-1])
    
    # # new_ct_namet1i = 'imginT1DUAL-'+pa.split('\\')[-1]
    # # save_pathnewt1i=save_path_Tidualimgin+new_ct_namet1i
    # # if not os.path.exists(save_pathnewt1i):
    # #     os.makedirs(save_pathnewt1i)
    # #sitk.WriteImage(maskctp,save_pathnewt1i)
    # #sitk.WriteImage(maskctp,os.path.join(save_pathnewt1i ,'imgT1DUAL'+pa.split('\\')[-1]+'.nii'))
    # sitk.WriteImage(maskctp,os.path.join(save_pathnewt1i ,'data'+'.nii'+'.gz'))
    
    # read dcm image for T1DUAL and store as volume for each subject for outphase
    reader2 = sitk.ImageSeriesReader()
    reader2.SetFileNames(lstFilesT1DUALOutphase)
    maskctpo= reader2.Execute()
    #save_path=os.path.join(mask_save,datadir.split('\\')[-1])
    
    
    readerm2 = sitk.ImageSeriesReader()
    readerm2.SetFileNames(lstFilesT1DUALmask)
    maskctm2= readerm2.Execute()
    ndammm2 = sitk.GetArrayFromImage(maskctm2)
    ndammm2[ndammm2==63]=1
    ndammm2[ndammm2==126]=2
    ndammm2[ndammm2==189]=3
    ndammm2[ndammm2==252]=4
    
    maskct2 = sitk.GetImageFromArray(ndammm2)
    #save_path=os.path.join(mask_save,datadir.split('\\')[-1])
    
    new_ct_namem = 'imgoutT1DUAL-'+pa.split('\\')[-1]
    save_pathnewt1i=save_path_Tidualimgout+new_ct_namem
    if not os.path.exists(save_pathnewt1i):
        os.makedirs(save_pathnewt1i)
    
    #sitk.WriteImage(maskct2,os.path.join(save_pathnew21 ,'maskT1DUAL'+pa.split('\\')[-1]+'.nii'))
    sitk.WriteImage(maskct2,os.path.join(save_pathnewt1i ,'label'+'.nii'+'.gz'))
    
    # new_ct_namet1o = 'imgoutT1DUAL-'+pa.split('\\')[-1]+ '.nii'
    # save_pathnewt1o=save_path_Tidualimgout+new_ct_namet1o
    # if not os.path.exists(save_pathnewt1o):
    #     os.makedirs(save_pathnewt1o)
    #sitk.WriteImage(maskctp,save_pathnewt1i)
    #sitk.WriteImage(maskctpo,os.path.join(save_pathnewt1o ,'imgT1DUAL'+pa.split('\\')[-1]+'.nii'))
    sitk.WriteImage(maskctpo,os.path.join(save_pathnewt1i ,'data'+'.nii'+'.gz'))
    
    #sitk.WriteImage(maskct,save_pathnewt1o)
    
#%% convert dicom to nifiti for choas dataset using dicom2nifti librarey
import os
import cv2
#import png
import pydicom
import numpy as np
from pydicom.tag import Tag
import time
import glob
from skimage import io, exposure, img_as_uint, img_as_float
foldername='D:\\covid2020segmentation\\CHAOS2019\\CHAOS_Train_Sets\\Train_Sets\\1\\T1DUAL\\DICOM_anon\\OutPhase'
FoldersPath='D:\\covid2020segmentation\\CHAOS2019\\CHAOS_Train_Sets\\Train_Sets\\1\\T1DUAL\\T1DUAL2'
#FolderList=glob.glob(os.path.join(FoldersPath,'**'))
PNG = False
FolderList=os.listdir(FoldersPath)
import dicom2nifti
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
#FolderList.remove('dcm2png.py')
import natsort
#d = 1
for Folder in FolderList:
    SubFolders=glob.glob(os.path.join(FoldersPath+'\\'+Folder,'*','*'))
    # for f in SubFolders:
    #     print(f)
#    if not os.path.exists(foldername+'\\'+Folder):
#            os.mkdir(foldername+'\\'+Folder)
    d=1
    for file in SubFolders:
        print(file)
        # file1=glob.glob(os.path.join(FoldersPath+'\\'+Folder+'\\'+file,'*'))
        # file2=str(file1)
        pathf=foldername+'\\'+Folder
        createFolder(pathf)
        dicom2nifti.dicom_series_to_nifti(file, pathf, reorient_nifti=True)
            
    #print(foldername)
    
dicom2nifti.dicom_series_to_nifti(foldername, FoldersPath, reorient_nifti=True)


