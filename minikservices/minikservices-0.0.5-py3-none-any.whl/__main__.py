
from kservice.k8s_utils import MK
from kservice.arguments import parse_arguments


def main():
    
    minikube = MK()

    # Check if minikube cluster is running
    if (minikube.check_cluster()) is not True:
        print("Minikube is not running. Exit.")
        exit(0)
    

    service_list = minikube.get_services()


    arguments = parse_arguments()

    arguments.print_usage()

    args = arguments.parse_args()
    



    print("\nListing services and their namespaces:")
    for s in service_list:
        print(f"Service: {s.name} {{{s.namespace}}}")







    
if __name__ == "__main__":
    main()