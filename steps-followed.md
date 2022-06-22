### Spin Up The Local K8s Cluster
* kind create cluster --name airflow-cluster --config kind-cluster.yaml
* kind create cluster --name airflow-cluster --image kindest/node:v1.21.1


### Make sure that the cluster is working
* kind get clusters
* kubectl cluster-info --context kind-airflow-cluster


### If you want to delete the cluster
* kind delete cluster --name <cluster_name>


### Add Airflow Helm Repo to local environment
* helm repo add apache-airflow https://airflow.apache.org
* helm repo update


### Create k8s Namespace and Install Helm Chart
* export NAMESPACE=airflow-cluster-namespace
* microk8s kubectl create namespace $NAMESPACE
* export RELEASE_NAME=airflow-cluster-release
* helm install $RELEASE_NAME apache-airflow/airflow --namespace $NAMESPACE --debug

### Forward the webserver to localhost:8080

#### First wait for the webserver pod to compeltely boot up
* microk8s kubectl get pods --namespace airflow-cluster-namespace -w
* microk8s kubectl port-forward svc/airflow-webserver 8080:8080 --namespace $NAMESPACE

### Get airflow values from helm
* helm show values apache-airflow/airflow > values.yaml

### After updating helm values.yaml, apply the changes to airflow on k8s
* helm upgrade --install airflow apache-airflow/airflow -n airflow-cluster-namespace -f values.yaml --debug

### Build Dockerfile
* sudo docker build -t airflow-custom:1.0.0 .

### import Docker image into the K8s cluster
* docker save <image_name> > <image_name>.tar
* microk8s ctr image import <image_name>.tar


### Create Airflow superuser
# create an admin user
* airflow users create \
    --username admin \
    --firstname Steve \
    --lastname Baca \
    --role Admin \
    --email smbaca99@gmail.com



