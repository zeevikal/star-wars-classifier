from scipy import ndimage, misc
import tensorflow as tf
import numpy as np
import sys

image_path = sys.argv[1]
# image_data = tf.gfile.FastGFile(image_path, 'rb').read()
# image_data = Image.open('{0}'.format(image_path))
image_data = ndimage.imread(image_path, mode="RGB")
image_data = misc.imresize(image_data, (299, 299))
image_data = np.array(image_data.reshape(1, 299, 299, 3))

label_lines = [line.rstrip() for line in tf.gfile.GFile("retrained_labels.txt")]

with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

# for op in tf.get_default_graph().get_operations():
#     print(str(op.name))

with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    predictions = sess.run(softmax_tensor,
                           {'Placeholder:0': image_data})
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))
