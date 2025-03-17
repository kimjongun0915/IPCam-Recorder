# 🎥 IPCam-Recorder

IPCam-Recorder는 OpenCV를 이용하여 **IP 카메라의 실시간 영상을 스트리밍하고, 녹화할 수 있는 Python 프로그램**입니다.  
녹화된 영상이 실제 녹화 시간과 동일한 길이로 저장되도록 FPS를 조정하는 기능이 포함되어 있습니다.

## 📌 주요 기능 (Features)
✅ **IP 카메라 스트리밍** - OpenCV를 사용하여 실시간 영상 표시  
✅ **영상 녹화 기능** - XVID 코덱을 사용하여 `AVI` 포맷으로 저장  
✅ **정확한 FPS 유지** - 녹화된 영상의 시간이 실제 녹화 시간과 일치  
✅ **녹화 상태 표시** - 녹화 중일 때 화면에 빨간 원과 경과 시간 출력  
✅ **키보드 컨트롤 지원** - `SPACE` 키로 녹화 시작/중지, `ESC` 키로 종료  

---

## ⚙️ 설치 방법 (Installation)
이 프로젝트를 실행하기 위해 **Python 3.12** 이상이 필요합니다.  
먼저, OpenCV를 설치하세요.

```bash
pip install opencv-python
