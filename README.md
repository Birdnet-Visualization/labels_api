# Labels API

## Run
- Enter to the Linode server by ssh
```
    ssh root@172.233.15.108
```
- Run the Docker
```
    cd labels_api
    docker-compose up --build -d
```

## Helpful commands
- Down the containers
```
    docker-compose down -v --remove-orphans
```

- Enter to mongo and delete data
```
    docker exec -it labels_api_mongo_1 bash
    mongosh mongodb://<USER>:<PASS>@mongo:27017/labels
    db.label.countDocuments()
    db.label.remove
    db.label.deleteMany({})
```