import cv2 as cv
import time

# IP 카메라 주소 입력
IP_CAMERA_URL = 'http://210.99.70.120:1935/live/cctv001.stream/playlist.m3u8'
cap = cv.VideoCapture(IP_CAMERA_URL)

# 비디오 저장 설정
fourcc = cv.VideoWriter_fourcc(*'XVID')  # 코덱 설정
out = None  # VideoWriter 객체 (초기값: None)

recording = False  # 녹화 상태
start_time = None  # 녹화 시작 시간
last_saved_time = 0  # 마지막으로 저장한 프레임 시간
fps = 20.0  # 목표 FPS
frame_interval = 1 / fps  # 프레임 저장 간격

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()  # 현재 시간
    
    # 녹화 중일 경우, 동영상 파일에 프레임 저장
    if recording:
        if out is None:
            # 동영상 저장 파일 생성 (FPS: 20, 해상도: 원본 크기)
            frame_size = (frame.shape[1], frame.shape[0])
            out = cv.VideoWriter('output.avi', fourcc, fps, frame_size)
            start_time = current_time
            last_saved_time = current_time  # 첫 프레임 저장 시간 초기화
        
        # 정확한 FPS 간격으로 프레임 저장
        if current_time - last_saved_time >= frame_interval:
            out.write(frame)
            last_saved_time = current_time  # 마지막 저장 시간 업데이트

        # 경과 시간 표시
        elapsed_time = int(current_time - start_time)
        cv.putText(frame, f"Time: {elapsed_time}s", (10, 465), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # 화면에 빨간색 원 표시 (녹화 중 시각적 효과)
        cv.circle(frame, (25, 25), 10, (0, 0, 255), -1)

    # 화면에 출력
    cv.imshow('IP Camera', frame)

    # 키 입력 처리
    key = cv.waitKey(1) & 0xFF
    if key == 27:  # ESC 키: 종료
        break
    elif key == 32:  # SPACE 키: 녹화 모드 변경
        recording = not recording
        if not recording and out is not None:
            out.release()
            out = None

# 자원 해제
cap.release()
if out is not None:
    out.release()
cv.destroyAllWindows()
