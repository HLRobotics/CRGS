from firebase import firebase


firCon="https://swarm-98ef3-default-rtdb.firebaseio.com/"

firebase = firebase.FirebaseApplication(firCon, None)
firebase.put('/direction/','Direction','R000R100')
print('Record Updated')