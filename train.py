import tensorflow.keras.utils
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D, concatenate
from tensorflow.keras import Model

def create_cnn_model():
    # Creating the model

    enc_conv0 = Conv2D(32, (3, 3), padding="same",activation='relu', kernel_initializer="he_normal")(inputs)
    enc_conv1 = Conv2D(32,(3,3),padding="SAME",activation='relu')(enc_conv0)
    max_pool1 = MaxPooling2D((2,2))(enc_conv1)

    # TODO verificar pesos de entrada
    enc_conv2 = Conv2D(32,(3,3),padding="SAME",activation='relu')(max_pool1)
    max_pool2 = MaxPooling2D((2,2))(enc_conv2)

    enc_conv3 = Conv2D(32,(3,3),padding="SAME",activation='relu')(max_pool2)
    max_pool3 = MaxPooling2D((2,2))(enc_conv3)

    enc_conv4 = Conv2D(32,(3,3),padding="SAME",activation='relu')(max_pool3)
    max_pool4 = MaxPooling2D((2,2))(enc_conv4)

    enc_conv5 = Conv2D(32,(3,3),padding="SAME",activation='relu')(max_pool4)
    max_pool5 = MaxPooling2D((2,2))(enc_conv5)

    enc_conv6 = Conv2D(32,(3,3),padding="SAME",activation='relu')(max_pool5)

    up_samp5 = UpSampling2D((2,2))(enc_conv6)
    concat_5 = concatenate([up_samp5,max_pool4])

    dec_conv5a = Conv2D(64,(3,3),padding="SAME",activation='relu')(concat_5)
    dec_conv5b = Conv2D(64,(3,3),padding='SAME',activation='relu')(dec_conv5a)

    up_samp4 = UpSampling2D((2,2))(dec_conv5b)
    concat_4 = concatenate([up_samp4,max_pool3])

    dec_conv4a = Conv2D(64,(3,3),padding="SAME",activation='relu')(concat_4)
    dec_conv4b = Conv2D(64,(3,3),padding='SAME',activation='relu')(dec_conv4a)

    up_samp3 = UpSampling2D((2,2))(dec_conv4b)
    concat_3 = concatenate([up_samp3,max_pool2])

    dec_conv3a = Conv2D(64,(3,3),padding="SAME",activation='relu')(concat_3)
    dec_conv3b = Conv2D(64,(3,3),padding='SAME',activation='relu')(dec_conv3a)

    up_samp2 = UpSampling2D((2,2))(dec_conv3b)
    concat_2 = concatenate([up_samp2,max_pool1])

    dec_conv2a = Conv2D(64,(3,3),padding="SAME",activation='relu')(concat_2)
    dec_conv2b = Conv2D(64,(3,3),padding='SAME',activation='relu')(dec_conv2a)

    up_samp1 = UpSampling2D((2,2))(dec_conv2b)
    concat_1 = concatenate([up_samp1,inputs])

    dec_conv1a = Conv2D(64,(3,3),padding="SAME",activation='relu')(concat_1)
    dec_conv1b = Conv2D(32,(3,3),padding='SAME',activation='relu')(dec_conv1a)
    dec_conv1c = Conv2D(2,(3,3),padding='SAME',activation='linear')(dec_conv1b)

    model = Model(inputs=inputs,outputs=dec_conv1c)
    return model

if __name__ == '__main__':
    model = create_cnn_model()
    model.summary()