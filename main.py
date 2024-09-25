import classes as cl
data = cl.Json.load_json()

res = cl.Json.data_to_dict(data)
print(res)
