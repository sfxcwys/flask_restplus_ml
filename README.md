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

## Hosting the Swagger UI publicly

After you've tested the Swagger UI locally, you may want to share it with your colleagues. One way to achieve that is to make the Swagger UI publicly accessible by making use of [ngrok](https://ngrok.com/).

1. Download ngrok from https://ngrok.com/ (you may first need to create a free account with ngrok) and follow the instruction on their webpage to unzip the downloaded file
2. Run the docker container locally, in this example we will run the container with `host IP=0.0.0.0` and `host port=8000`
3. On terminal, navigate to the folder where you unzip the downloaded ngrok file, then run the following command
```./ngrok http 8000```
4. The terminal will pop up something that looks like
```
Session Status                online
Session Expires               5 hours, 31 minutes
Version                       2.2.8
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://b222b731.ngrok.io -> localhost:8000
Forwarding                    https://b222b731.ngrok.io -> localhost:8000
```
5. The part `http://b222b731.ngrok.io -> localhost:8000` means requests to `http://b222b731.ngrok.io` are now being forwarded by ngrok to `localhost:8000`, therefore your Swagger UI is now publicly available at `http://b222b731.ngrok.io`

For more examples of using ngrok, please visit [this](https://www.twilio.com/blog/2016/12/localhost-tunneling-ngrok-mac-os-x.html) nice blog post.
