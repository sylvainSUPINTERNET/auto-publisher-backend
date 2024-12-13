# Start backend 

```` bash

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
# use default queue ( celery named )
# Windows ( fork() is not working ... must use solo or another alternative )
cd workers ;; celery -A app_worker worker --loglevel=debug -P solo

# Feel free to add queues names instead of using default celery  ( define at @task decorator)
cd workers ;; celery -A app_worker worker --loglevel=debug -P solo -Q MY_QUEUE_NAME


# UNIX
cd workers && celery -A app_worker worker --loglevel=debug --concurrency=8
````


# Start consumers 

```bash
# Package name
python -m consumers.yt_dl_consumer

```

