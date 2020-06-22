# Prophet Inference: An inference only fork of Prophet (Python only)

This is an inference only fork of Prophet for Python. 

As the name suggests, this is a stripped down version of Prophet that supports only inferencing from a fitted Prophet model.

The primary purpose of this package is to deploy a Prophet model in a light weight environment for the purpose of inference/prediction. This implementation does not require heavy dependencies such as pystan(Stan) and Cython which requires a C/C++ compiler. It is a purely Python based and does not require additional binaries.

In most cases, training the Prophet model is done on a development environment such as Jupyter Notebooks or Python scripts and rarely in a deployment environment. This package can be installed in the deployment environment easily and perform inference/predictions from the earlier developed models.

In summary, the main changes are,
- removed dependencies Cython, cmdstanpy and pystan from requirements.txt
- commented out Stan related code

Refer to the [original implementation] (https://facebook.github.io/prophet/) for more details.


## Installation in Python

Prophet Inference is on PyPI, so you can use `pip` to install it.

```bash
pip install fbprophet
```

Train the Prophet model and export model parameters

```bash
# create and fit model
df = pd.read_csv("data.csv")
m = Prophet()
m.fit(df)
# export data to json using fbprophet_inference
model_json = fbprophet_inference.serialize.model_to_json(m)
```

Import model parameters and call the predict functions

```bash
# Remember that this is an inference-only instance of Prophet and you should only call the predict function.
model = fbprophet_inference.serialize.model_from_json(model_json)
model.predict(df)
```

Prophet Inference is licensed under the [MIT license](LICENSE.md).
