# Start backend 

```` bash

# conda or venv
python -m venv auto-publisher-env

python -m pip install -r requirements.txt

````	


```` bash
# dev 
fastapi dev 

# prod
fastapi run

````

# Start workers

```` bash 

# Windows
celery -A workers.app_worker worker --loglevel=debug -P solo -Q yt.download,whisper.transcribe

# UNIX
celery -A workers.app_worker worker --loglevel=debug --concurrency=8 -Q yt.download,whisper.transcribe


# # use default queue ( celery named )
# # Windows ( fork() is not working ... must use solo or another alternative )
# cd workers ;; celery -A app_worker worker --loglevel=debug -P solo

# # Feel free to add queues names instead of using default celery  ( define at @task decorator)
# cd workers ;; celery -A app_worker worker --loglevel=debug -P solo -Q EXAMPLE_Q


# UNIX
cd workers && celery -A app_worker worker --loglevel=debug --concurrency=8
````


# Start consumers 

```bash
# Package name
python -m consumers.yt_dl_consumer

```



https://gist.github.com/sylvainSUPINTERNET/f78ed3243e9d4c1e9f782b8e2a47e536