import requests


BASE_URL = "http://127.0.0.1:5000/advertisements/"

#create new advertisement
response = requests.post(BASE_URL,
    json={'title':'Продам автомобиль',
          'description': 'VW Passat',
          'owner': 'owner1'})

print(response.status_code)
print(response.json())

#update advertisement
response = requests.patch(BASE_URL + '1',
    json={
          'description': 'VW Passat - новый'
          })

print(response.status_code)
print(response.json())


#delete advertisement
response = requests.delete(BASE_URL + '1')

print(response.status_code)
print(response.json())

#get advertisement
response = requests.get(BASE_URL + '1')

print(response.status_code)
print(response.json())