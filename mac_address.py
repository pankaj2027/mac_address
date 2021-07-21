import requests
import sys

def company_name(url):
    data = requests.get(url,verify=False)
    data_json = data.json()
    if data_json["macAddressDetails"]["isValid"] == 'true':
        company_name_1 = data_json['vendorDetails']['companyName']
    else:
        company_name_1 = "Mac address is not valid.."
    return company_name_1
    
try:
    url  = "https://api.macaddress.io/v1?apiKey=at_BHA58QvWvCa6iT1lv9nSfL9q5JtJg&output=json&search={}".format(sys.argv[1])
    company = company_name(url)
    print(company)
except:
    print('Error: Mac address is not found!!!')