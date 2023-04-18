# microservice-calculator

Simple calculator application that uses microservices to perform mathematical operations. It is the project coursework for UE20CS351 - Cloud Computing. The problem statement can be found [here](https://github.com/ta-cc-2023/UE20CS351-Cloud-Computing-Problem-Statements/tree/main/Project-4).

### Project Report


The microservice based calculator project consists of a backend directory containing individual microservices for performing mathematical operations such as addition, division, greater than, lesser than, etc. Each of these services has its own Dockerfile and a requirements.txt file for installing dependencies.

The frontend directory contains the Flask application responsible for routing user requests to the appropriate microservice. The frontend also has a Dockerfile and a requirements.txt file for building and running the Flask application. The templates folder within the frontend directory contains an HTML file for the user interface.

The project is orchestrated using docker-compose.yml file. When running the project, docker-compose builds the necessary Docker images and starts the containers for each microservice and the frontend. The project can be accessed through the web browser.

Overall, the project provides a scalable, distributed architecture for a calculator application. The project can be extended with additional microservices and features as needed. The images directory contains screenshots of the application options and the application operation.

### Team

| **Name**          | **SRN**       |
|-------------------|---------------|
| Aryan Rawther     | PES1UG20CS082 |
| Aryan V S         | PES1UG20CS083 |
| Aryansh Bhargavan | PES1UG20CS084 |
| Ashish Kulkarni   | PES1UG20CS085 |

### Prerequisites
- Docker
- Python 3

### Installing

```
git clone https://github.com/a-r-r-o-w/microservice-calculator
cd microservice-calculator
```

### Screenshots

**Starting Application**

```
docker-compose up -d
# Note that first run may take some time as docker will install
# required images and set up microservices one by one
```

![starting-application.png](./images/starting-application.png)

<br />

**Using Application**

![application-options.png](./images/application-options.png)

<br />

![application-operation.png](./images/application-operation.png)

<br />

**Stopping Application**

```
docker-compose down --rmi all -v --remove-orphans
```

![stopping-application.png](./images/stopping-application.png)
