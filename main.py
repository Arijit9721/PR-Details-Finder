import requests

# get the data from the repo
url = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'
response = requests.get(url)
data = response.json()

#print the details of all the pull requests
for i in range(len(data)):
    print(" Serial Number:{} \n login_name:{} \n login_id:{} \n pull_request_url:{} \n pull_request_id:{} \n".format(i,data[i]["user"]["login"],data[i]["user"]["id"],data[i]["url"],data[i]["id"]))    

# find the number of pull requests made by each user
pull_count = {}
for i in range(len(data)):
    key = data[i]["user"]["login"]
    if key in pull_count:
        pull_count[key] += 1
    else:
        pull_count[key] = 1

print(pull_count)
