import fiftyone as fo

dataset = fo.load_dataset("coco-2017-validation")
session = fo.launch_app(dataset)
session.wait()
