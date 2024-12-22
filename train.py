from ultralytics import YOLO

# Load a model
model_yaml ="yolov8-seg.yaml"
data_yaml = "custom1.yaml"
model = YOLO(model_yaml)  # build a new model from YAML
model = YOLO('yolov8n-seg.pt')  # load a pretrained model (recommended for training)
model = YOLO(model_yaml).load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
model.train(data=data_yaml, epochs=100, imgsz=640, batch=128)
