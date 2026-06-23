import pandas as pd
from PIL import Image
from pathlib import Path
from collections import defaultdict

# Class Mapping
CLASS_MAP = {
    "articulated_truck": 0,
    "bicycle": 1,
    "bus": 2,
    "car": 3,
    "motorcycle": 4,
    "motorized_vehicle": 5,
    "non-motorized_vehicle": 6,
    "pedestrian": 7,
    "pickup_truck": 8,
    "single_unit_truck": 9,
    "work_van": 10
}

# Read labels
df = pd.read_csv("datasets/labels.csv", header=None)

df.columns = [
    "image_id",
    "vehicle_class",
    "xmin",
    "ymin",
    "xmax",
    "ymax"
]

# Create output folder
labels_dir = Path("yolo_dataset/labels")
labels_dir.mkdir(parents=True, exist_ok=True)

# Group annotations by image
grouped = defaultdict(list)

for _, row in df.iterrows():

    image_id = str(row["image_id"]).zfill(8)

    grouped[image_id].append(row)

# Convert
for image_id, annotations in grouped.items():

    image_path = Path(f"datasets/Images/{image_id}.jpg")

    if not image_path.exists():
        continue

    width, height = Image.open(image_path).size

    output_lines = []

    for row in annotations:

        class_id = CLASS_MAP[row["vehicle_class"]]

        xmin = row["xmin"]
        ymin = row["ymin"]
        xmax = row["xmax"]
        ymax = row["ymax"]

        x_center = ((xmin + xmax) / 2) / width
        y_center = ((ymin + ymax) / 2) / height

        box_width = (xmax - xmin) / width
        box_height = (ymax - ymin) / height

        output_lines.append(
            f"{class_id} "
            f"{x_center:.6f} "
            f"{y_center:.6f} "
            f"{box_width:.6f} "
            f"{box_height:.6f}"
        )

    with open(labels_dir / f"{image_id}.txt", "w") as f:
        f.write("\n".join(output_lines))

print("YOLO labels created successfully!")
print(f"Total label files: {len(grouped)}")