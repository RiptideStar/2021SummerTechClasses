import requests  #pip install requests

def classify(numbers):
    key = "f1360380-1c90-11ec-807b-6df81147aca3f7876008-6900-403a-bd20-ef6a0e2d088f"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"

    response = requests.post(url, json={"data": numbers})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

data1 = input("Passenger Ticket Class: ")               #ticket class
data2 = input("gender (0: male; 1: female): ")          #gender
if (data2 == '0'):
    data2 = "male"
else: 
    data2 = "female"    
data3 = input("Age: ")               #age
data4 = input("# of Siblings: ")               #sibling
data5 = input("# of Parents/Children: ")               #parental units/childrenal units
data6 = input("Ticket Fare $: ")             #ticket fare
data7 = input("Location Embarked:\n1: Cherbourg\n2. Queenstown\n3. SouthHampton\nType your number here: ")    #location embarked
switcher = {
    1: "Cherbourg",
    2: "Queenstwn"
}
data7 = switcher.get(data7, "SouthHampt")

test_data = [ data1, data2, data3, data4, data5, data6, data7 ]

demo = classify(test_data)

label = demo["class_name"]
confidence = demo["confidence"]

# print(f"Passenger Info: gender: {data2} age: {data3} ticket class: {data1}")
print("result: '%s' with %d%% confidence" % (label, confidence))