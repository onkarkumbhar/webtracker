import requests
import wget
import os

# getting directories from list
f = open('test_dirlist.txt','r')
data = f.read().split('\n')
f.close()
f = open('extensions.txt','r')
ex = f.read().split('\n')
f.close()

url = input("Enter URL(https://example.com/): ")

f1 = open("requests.txt","w")
for i in data:
    for j in ex:
        url1 = url+i+j
        response = requests.get(url1)
        f1.write(url1+"    "+str(response.status_code)+"\n")
        if response.status_code != 404:
            f = open('output.txt','a')
            f.write(url1+"      "+str(response.status_code)+'\n')
            f.close()
f1.close()


# httrack
try:
    os.mkdir("output")
except:
    pass

f = open("output.txt","r")
data = f.read().split("\n")
f.close()

# Download files from internet
for i in data:
    url1 = i.split("      ")[0]
    if url1 != "":
        filename = wget.download(url1, out="output")
    check_url_file = open(filename,"r")
    while True:
        line = check_url_file.readline()
        if not line:
            break
        temp = line.strip()
        for j in ex:
            if j in temp and j != "":
                print(temp)
                break
        if "href" in temp:
            found_url = temp.split("\">")[0].split("href=\"")[-1]
            if ".com" in found_url:
                print("*** page redirects to => "+found_url)
            else:
                f = open("output.txt","a")
                f.write(url + found_url+"      \n")
                f.write(url+"/"+found_url+"      \n")
                data.append(url + found_url+"      200")
                # data.append(url+"/"+found_url)
                f.close()
        
    check_url_file.close()