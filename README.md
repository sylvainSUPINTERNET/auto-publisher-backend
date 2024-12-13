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
cd workers && celery -A app_worker worker --loglevel=info --concurrency=8
````


# Start consumers 

```bash
# Package name
python -m consumers.yt_dl_consumer

```

