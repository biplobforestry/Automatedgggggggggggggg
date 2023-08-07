Here,
#file_1
"Resizing images" for resizing the orginal images into 224x224

#file_2
In "Train and testing ", you can use this structure for any pre-trained model available in TensorFlow Keras, such as MobileNet, ResNet50.
You would just need to replace "VGG16" with the name of the model you want to use.

For example, if you want to use the MobileNet model, you could replace "VGG16" with "MobileNet", like this:
from tensorflow.keras.applications import MobileNet

mobilenet = MobileNet(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet",
    pooling='avg'
)

mobilenet.trainable = False


Similarly, if you want to use the ResNet50 model, you could replace "VGG16" with "ResNet50", like this:
from tensorflow.keras.applications import ResNet50

resnet50 = ResNet50(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet",
    pooling='avg'
)

resnet50.trainable = False

#file_3 
"Model deploy" is for testing the trained model with unseen dataset
