import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "coco-2017",
    split="validation",
    label_types=["detections"],
    classes=["person", "cell phone"],
    max_samples=800,
    shuffle=True,
    seed=42,
    dataset_name="exam_cheating_coco"   # ⭐ THIS SAVES IT
)

session = fo.launch_app(dataset)
session.wait()
