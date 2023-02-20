import requests
import json
# Project & Token Values
project_name = "proj_name"
region = "locations"
instance_name = "instance_name"
access_token = "access_token"

# Get the CDAP Enpoint with Namespace as argument
def get_CDAP_endpoint_pip(name_space):
    cdap_build = f"api_endpoint/{name_space}/apps/"
    cdap_url=f"{cdap_build}"
    cdap_response = requests.get(cdap_url, headers=headers)
    if cdap_response.status_code == 200:
        # print(cdap_response.json()) # Print the response content as JSON
        pipeline_name_data = cdap_response.json()
        for item in pipeline_name_data:
            try:
                pipeline_name = item['name']
                print("")
                print("Pipeline Name is ",pipeline_name)
                cdap_endpoint = f"api_endpoint/{name_space}/apps/{pipeline_name}/workflows/DataPipelineWorkflow/runs"
                # print(cdap_endpoint)
                cdap_url=f"{cdap_endpoint}"
                cdap_response = requests.get(cdap_url, headers=headers)
                # print(cdap_response.json()) # Print the response content as JSON
                pipeline_data = cdap_response.json()
            except json.JSONDecodeError:
                print(f"Skipping pipeline{item['name']} because key fields are missing")
                continue    
            for item in pipeline_data:
                try:
                    runid, starting, end, numNodes = item['runid'], item['starting'], item['end'], item['cluster']['numNodes']
                    # print(runid, starting, end, numNodes)
                    total_run_secs = end - starting
                    print("Run ID", runid)
                    print("Ran for ", total_run_secs, " secs")
                    print("numNodes ", numNodes)

                except KeyError:
                    print(f"Skipping record with runid {item['runid']} because it has no 'numNodes' field")
                    continue                             
    else:
        print(f"Error: {cdap_response.status_code} - {cdap_response.text}") # Print the error message

# Make the API request to get the Namespace
url = f"https://datafusion.googleapis.com/v1beta1/projects/{project_name}/locations/{region}/instances/{instance_name}/namespaces/"
# print(url)
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(url, headers=headers)
# print(response)

# Extract namespace IDs from response
if response.status_code == 200:
    namespaces = response.json()["namespaces"]
    for namespace in namespaces:
        print("")
        print(f"Entering Namespace : {namespace['name']} & Retrieving Pipeline details")
        print("====================================================================")
        print("")
        name_space=namespace['name']
        get_CDAP_endpoint_pip(name_space)
else:
    print(f"Error retrieving namespaces: {response.headers}")