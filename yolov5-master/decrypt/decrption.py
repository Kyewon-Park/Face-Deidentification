import cv2
import glob
import os
import numpy as np

script_dir = os.path.dirname(__file__)
#텍스트파일 읽기
rel_path="/labels/*.txt"
txt_files = sorted(glob.glob(script_dir + rel_path),key=len)
#영상파일 읽기
vidcap = cv2.VideoCapture(script_dir +"/hfyu1.avi")
# vidcap = cv2.VideoCapture(script_dir +"/0.mp4")
#노이즈 사진 읽기
noise_original = cv2.imread('noise.png') # cd decrypt 후 사용

count_in_list = 0
frame_count=0

#사진 저장 변수
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
w = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = vidcap.get(cv2.CAP_PROP_FPS)
fps = 20
out = cv2.VideoWriter(script_dir +"/output.avi", fourcc, fps, (w, h))

while vidcap.isOpened():
    #프레임 하나 당 텍스트 파일 하나 꺼내서 읽어 수정 
    success, frame = vidcap.read()    
    # fps, w, h = vidcap.get(cv2.CAP_PROP_FPS), frame.shape[1], frame.shape[0]
    if not success:
        print("read fail - video ends")
        break
    #텍스트 파일 꺼내서 앞에 파일이름 숫자 받음
    file_name = txt_files[count_in_list]
    file_num = int(file_name.split("labels\\")[1].split('.')[0])
    print(f"file_num = {file_num}")
    print(f"frame_count = {frame_count}")
    
    #frame_count가 리스트 위치 count보다 낮음 = 찾은 얼굴이 없는 상태
    #숫자랑 frame_count랑 불일치하면 
    if file_num != frame_count:
        for i in range(file_num - frame_count):
            print(f"pass frame {i} times")
            
            out.write(frame)
            success, frame = vidcap.read()
            frame_count+=1             
            
            if file_num==frame_count:
                print(f"count is same - break: {file_num}")
                break
                
            cv2.imshow("after",frame)
            cv2.waitKey(1)
            continue
            ########
        
        print(f"after pass : frame_count = {frame_count}")
        
    with open(file_name, "r") as fd:
        for xyxy in fd.readlines():
            coord=list(map(int,xyxy[2:-1].split())) # ex: [236, 146, 369, 329]
            print(f"coord = {coord}")
            noise = noise_original[coord[1]:coord[3],coord[0]:coord[2]] #노이즈 부분
            encrypted_region = frame[coord[1]:coord[3],coord[0]:coord[2]] #얼굴 부분            
            
            # #encrypted_region에서 noise 9/10 밝기값 뺌
            # noise = noise*0.9   
            # noise=np.trunc(noise)

            # print(f"encrypted_region = {encrypted_region[0][0]}")
            # print(f"noise = {noise[0][0]}")
            # faint_face= encrypted_region-noise                   
            # print(f"faint_face = {faint_face[0][0]}")
            
            # #10배를 곱함
            # face = faint_face*10

            #XOR
            xored=encrypted_region #배열 초기화
            for h in range(len(noise)):
                for j in range(len(noise[0])):
                    for k in range(3):
                        xored[h][j][k]=encrypted_region[h][j][k]^noise[h][j][k]
            frame[coord[1]:coord[3],coord[0]:coord[2]]=xored

    out.write(frame)
    cv2.imshow("after",frame)
    cv2.waitKey(1)

    count_in_list += 1
    frame_count += 1

vidcap.release()
out.release()
