# star-wars-classifier
Darth Vader and Yoda classifier with TensorFlow


### retraining session:
```
python retrain.py \
--bottleneck_dir=bottlenecks \
--how_many_training_steps 500 \
--model_dir=inception \
--output_graph=retrained_graph.pb \
--output_labels=retrained_labels.txt \
--image_dir images
```
