import tensorflow as tf


def create_feature_extractor(model, retain_outputs=False, layer_names=[], skip_first_N=0):
    layer_outputs = []
    sub_models = []

    for layer in model.layers:
        if isinstance(layer, tf.keras.models.Model):
            sub_model, skip_first_N = create_feature_extractor(layer, layer_names=[], skip_first_N=skip_first_N)
            sub_models.append(sub_model)
        if isinstance(layer, tf.keras.layers.Conv2D):
            if skip_first_N > 0:
                skip_first_N -= 1
            else:
                if (len(layer_names) == 0) or (layer.name in layer_names):
                    averaged_layer_outputs = tf.reduce_mean(layer.output, axis=[1, 2])
                    layer_outputs.append(averaged_layer_outputs)

    for sub_model in sub_models:
        sub_model_outputs = sub_model(model.inputs)
        if not isinstance(sub_model_outputs, list):
            sub_model_outputs = [sub_model_outputs]
        layer_outputs.extend(sub_model_outputs)

    model_outputs = None

    if retain_outputs:
        model_outputs = {"layer_outputs": layer_outputs, "model_outputs": model.outputs}
        return tf.keras.models.Model(inputs=model.inputs, outputs=model_outputs)
    else:
        model_outputs = layer_outputs
        return tf.keras.models.Model(inputs=model.inputs, outputs=model_outputs), skip_first_N



