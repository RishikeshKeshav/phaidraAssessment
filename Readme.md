

```markdown


This project demonstrates how to set up a scraping service using Prometheus and deploy it to Minikube.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Docker
- Minikube
- kubectl

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/RishikeshKeshav/phaidra-FastApi-prometheus.git
   cd repository
   ```

2. Create a `prometheus.yml` file with the Prometheus configuration.

3. Create a Dockerfile for your application (`main.py`) and build the Docker image:

4. Set up Docker Compose to manage your services. Example `docker-compose.yml`:



   ```bash
   docker-compose -f docker-compose.yaml up
   ```
5. Test your services locally using Docker Compose:

   ```bash
   docker-compose -f docker-compose.yaml down
   ```
 Access the scrapper service at http://localhost:8080 http://localhost:9095/metrics and Prometheus at http://localhost:9090.




6. Push your Docker images to Docker Hub:

   ```bash
   docker push iamrishikesh/app:latest
   ```

   ```bash
   docker push prom/prometheus:latest
   ```

7. Create Deployment YAML files for your application and Prometheus (`app.yaml` and `prom.yaml`).

8. Create Service YAML files for your application and Prometheus (`myappSvc.yaml` and `myprom.yaml`).

9. Deploy your application and Prometheus to Minikube:

   ```bash
   kubectl apply -f app.yaml
   ```

   ```bash
   kubectl apply -f prom.yaml
   ```
10. Create Services for app and prometheus
    ```bash
    kubectl apply -f myappSvc.yaml
    ```
    ```bash
    kubectl apply -f myprom.yaml
    ```
  
10. Access your services in Minikube:

    - Scrapper service: `minikube service fastapi-service --url`
    - Prometheus service: `minikube service promtheus-service --url`

11. Test your services using Minikube URLs and port forwarding:

    ```bash
    kubectl port-forward service/fastapi-service 8080:8080 9095:9095
    ```

    ```bash
    kubectl port-forward service/promtheus-service 9090:9090
    ```

    Access the scrapper service at http://localhost:8080 http://localhost:9095/metrics and Prometheus at http://localhost:9090
```
