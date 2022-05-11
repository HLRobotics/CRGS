from firebase import firebase
firCon="https://swarm-98ef3-default-rtdb.firebaseio.com/"

firebase=firebase.FirebaseApplication(firCon,None)

data =  "R100N100"

result = firebase.post('/direction/',data)
print(result)