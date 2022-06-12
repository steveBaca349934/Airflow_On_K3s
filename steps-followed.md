### Spin Up The Local K8s Cluster
* kind create cluster --name airflow-cluster --config kind-cluster.yaml
* kind create cluster --name airflow-cluster --image kindest/node:v1.21.1


### Make sure that the cluster is working
* kind get clusters
* kubectl cluster-info --context kind-kind

### If you want to delete the cluster
* kind delete cluster --name <cluster_name>


### Add Airflow Helm Repo to local environment
* helm repo add apache-airflow https://airflow.apache.org
* helm repo update

### Create k8s Namespace and Install Helm Chart
* export NAMESPACE=airflow-cluster-namespace
* kubectl create namespace $NAMESPACE
* export RELEASE_NAME=airflow-cluster-release
* helm install $RELEASE_NAME apache-airflow/airflow --namespace $NAMESPACE


