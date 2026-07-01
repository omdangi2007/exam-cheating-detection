import fiftyone as fo
import fiftyone.types as fot

# Load saved dataset
dataset = fo.load_dataset("exam_cheating_coco")

# Export path
export_dir = "yolo_dataset"

dataset.export(
    export_dir=export_dir,
    dataset_type=fot.YOLOv5Dataset,   # YOLOv5 format works for YOLOv8 too
    label_field="ground_truth",
)

print("✅ Export complete!")
