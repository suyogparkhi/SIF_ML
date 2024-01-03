import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import time

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values to between 0 and 1
    return img_array

def create_siamese_model(input_shape=(224, 224, 3)):
    base_model = tf.keras.applications.MobileNetV2(input_shape=input_shape, include_top=False, weights='imagenet')
    base_model.trainable = False

    input_a = layers.Input(shape=input_shape)
    input_b = layers.Input(shape=input_shape)

    # Feature extraction
    x = base_model(input_a)
    y = base_model(input_b)

    # Flatten and concatenate features
    x = layers.Flatten()(x)
    y = layers.Flatten()(y)
    concatenated = layers.Concatenate()([x, y])

    # Dense layers for similarity comparison
    dense1 = layers.Dense(512, activation='relu')(concatenated)
    dense2 = layers.Dense(256, activation='relu')(dense1)
    output = layers.Dense(1, activation='sigmoid')(dense2)

    model = models.Model(inputs=[input_a, input_b], outputs=output)
    return model

def generate_pairs(folder_path):
    pairs = []
    file_list = os.listdir(folder_path)
    for i, file1 in enumerate(file_list):
        for j, file2 in enumerate(file_list):
            if i < j:
                pairs.append((os.path.join(folder_path, file1), os.path.join(folder_path, file2)))
    return pairs

def create_data_generator(pair_paths, labels, batch_size=32):
    while True:
        for i in range(0, len(pair_paths), batch_size):
            batch_pairs = pair_paths[i:i+batch_size]
            batch_labels = labels[i:i+batch_size]
            x1 = [load_and_preprocess_image(pair[0]) for pair in batch_pairs]
            x2 = [load_and_preprocess_image(pair[1]) for pair in batch_pairs]
            y = np.array(batch_labels)
            yield ([np.array(x1), np.array(x2)], y)

# Set your dataset path
dataset_folder = 'path/to/your/dataset'

# Generate pairs and labels
pairs = generate_pairs(dataset_folder)
labels = [1] * len(pairs)  # All pairs are similar for training

# Create the Siamese model
siamese_model = create_siamese_model()

# Compile the model
siamese_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
batch_size = 32
epochs = 10
steps_per_epoch = len(pairs) // batch_size

# Create data generator
data_generator = create_data_generator(pairs, labels, batch_size=batch_size)

# Measure computing time
start_time = time.time()

# Train the model
siamese_model.fit(data_generator, steps_per_epoch=steps_per_epoch, epochs=epochs)

# Calculate and print the total computing time
end_time = time.time()
total_time = end_time - start_time
print(f"Total computing time: {total_time} seconds")

# Now you can use the trained model to predict similarity for new pairs.
