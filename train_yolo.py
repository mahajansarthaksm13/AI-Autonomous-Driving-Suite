from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="yolo_dataset/dataset.yaml",
    epochs=5,
    imgsz=640,
    batch=4,
    workers=0,
    device="cpu",
    project="runs",
    name="vehicle_detector_test"
)