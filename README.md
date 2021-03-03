# submission_service

## Create server

```
openapi-generator generate -i https://sage-bionetworks.github.io/submission-schemas/edge/openapi.json -g python-flask -o server -t .codegen/server
```

```
openapi-generator generate -i https://sage-bionetworks.github.io/submission-schemas/develop/openapi.yaml -g python-flask -o server
```

## Deploy using Docker

1. Create the file that contains the future environment variables
```
cp .env.sample .env
```
1. Start the Submission API service
```
docker-compose up --build
```
1. In your browser, go to the web service documentation page <http://localhost:8080/api/v1/ui/> to check that the web service of the Data. Node started successfully.