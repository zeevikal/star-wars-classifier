# star-wars-classifier
Darth Vader and Yoda classifier with TensorFlow

## Training & Prediction process:

#### downloading data:
you can use this awesome extension which can download all
google search image results [here](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en).

please save all images in `images` directory.

#### clean data:
```
python utils.py
```

#### retraining session:
```
python retrain.py \
--bottleneck_dir=bottlenecks \
--how_many_training_steps 500 \
--model_dir=inception \
--output_graph=retrained_graph.pb \
--output_labels=retrained_labels.txt \
--image_dir images
```
#### prediction session:
```
python predict.py example_image
```