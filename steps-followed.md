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
* kubectl create namespace $NAMESPACE
* export RELEASE_NAME=airflow-cluster-release
* helm install $RELEASE_NAME apache-airflow/airflow --namespace $NAMESPACE --debug

### Forward the webserver to localhost:8080

#### First wait for the webserver pod to compeltely boot up
* kubectl get pods --namespace airflow-cluster-namespace -w
* kubectl port-forward svc/$RELEASE_NAME-webserver 8080:8080 --namespace $NAMESPACE

