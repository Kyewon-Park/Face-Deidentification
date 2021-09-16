import cv2
import glob
import os

script_dir = os.path.dirname(__file__)
#텍스트파일 읽기
rel_path="/labels/*.txt"
txt_files = sorted(glob.glob(script_dir + rel_path),key=len)
#영상파일 읽기
vidcap = cv2.VideoCapture(script_dir +"/0.mp4")
#노이즈 사진 읽기
noise_original = cv2.imread('noise.png')

while vidcap.isOpened():
    #프레임 하나 당 텍스트 파일 하나 꺼내서 읽어 수정 
    success, frame = vidcap.read()
    if(not success):
        break
    fps, w, h = vidcap.get(cv2.CAP_PROP_FPS), frame.shape[1], frame.shape[0]
    out = cv2.VideoWriter(script_dir,cv2.VideoWriter_fourcc(*'mp4v'), fps, (w,h))
    out.write(frame)
    
out.release()

