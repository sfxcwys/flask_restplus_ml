# Deploying machine learning model using Flask RestPlus

This repo provides code of training a machine learning model using [sklearn Pipeline](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.pipeline) and deploying the trained model using [Flask RestPlus](https://flask-restplus.readthedocs.io/en/stable/).

Sklearn Pipeline is a useful tool for encapsulating multiple transformers together with an estimator into one object, so that important methods like `fit()` and `predict()` only needs to be called once. After the pipeline is trained we can pickle the object and add a Web API on top of it, that way the model can be consumed for scoring without needing to re-train it everytime.

Flask RestPlus provides a Web API for others to consume the model for scoring, it also provides a Swagger UI for others to interact with the model.

## Run with docker

**Build the docker image**
```
docker build --force-rm=true -t <image tag> .
```

**Run the docker container (if the container is run locally, use 0.0.0.0 for host IP)**
```
docker run -it --publish=<host port>:5000 --name=<container name> -e MODEL_HOST=<host IP> <image tag>
```

**Swagger UI**
```
http://<host IP>:<host port>
```
