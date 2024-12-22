data_yaml = "custom.yam"
yolo task=segment mode=train model=yolov8n-seg.pt imgsz=640 data=custom.yaml epochs=100 batch=64 name=yolov8n-seg exist_ok=True amp=False

