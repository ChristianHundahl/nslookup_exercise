import subprocess

domain_name = input("Enter the domain name: ")

command = "nslookup {}".format(domain_name)

#Prevent injection:
if len(command.split()) > 1:
    raise Exception("Input must be only one argument")

response = subprocess.check_output(command, shell=True, encoding="UTF-8")

print(response)

