import requests  #pip install requests

def classify(numbers):
    key = "7e63dcd0-1be4-11ec-8582-95bb29bbfa717727002d-ae9d-481e-b1f5-886059dcbc5d"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"

    response = requests.post(url, json={"data": numbers})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

data1 = 2               #ticket class
data2 = "male"          #gender
data3 = 7               #age
data4 = 1               #sibling
data5 = 0               #parental units/childrenal units
data6 = 200             #ticket fare
data7 = "Cherbourg"     #location embarked

test_data = [ data1, data2, data3, data4, data5, data6, data7 ]

demo = classify(test_data)

label = demo["class_name"]
confidence = demo["confidence"]

print(f"gender: {data2} age: {data3} ticket class: {data1}")
print("result: '%s' with %d%% confidence" % (label, confidence))