from pathlib import Path
import random
import shutil

random.seed(42)

images = list(Path("datasets/Images").glob("*.jpg"))

random.shuffle(images)

total = len(images)

train_end = int(total * 0.8)
val_end = int(total * 0.9)

train = images[:train_end]
val = images[train_end:val_end]
test = images[val_end:]

for split_name, split_data in [
    ("train", train),
    ("val", val),
    ("test", test)
]:

    img_dir = Path(f"yolo_dataset/images/{split_name}")
    lbl_dir = Path(f"yolo_dataset/labels/{split_name}")

    img_dir.mkdir(parents=True, exist_ok=True)
    lbl_dir.mkdir(parents=True, exist_ok=True)

    for img in split_data:

        shutil.copy(img, img_dir / img.name)

        label_file = Path(
            f"yolo_dataset/labels/{img.stem}.txt"
        )

        if label_file.exists():
            shutil.copy(
                label_file,
                lbl_dir / label_file.name
            )

print("Dataset Split Complete")

print(f"Train: {len(train)}")
print(f"Val: {len(val)}")
print(f"Test: {len(test)}")