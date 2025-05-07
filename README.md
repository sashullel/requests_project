# Make random requests!


## Overview

Hello!

This repository contains a Python script which makes 5 HTTP requests to the httpstat.us website and runs in a Docker contianer for ease of use.


## Getting started

### Clone the repository

```
git clone https://github.com/sashullel/requests_project
```

### Navigate to the directory
```
cd requests_project
```

Build the Docker image and run the Docker container
```
docker build -t requests_project -f docker/Dockerfile .
docker run requests_project
```

To get the container ID and see the logs
```
docker ps -a
docker logs <CONTAINER ID>
```
