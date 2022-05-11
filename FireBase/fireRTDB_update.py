def fireRTDB_push(Message):
    try:

        from firebase import firebase
        firCon="https://swarm-98ef3-default-rtdb.firebaseio.com/"

        firebase = firebase.FirebaseApplication(firCon, None)
        firebase.put('/direction/','Direction',Message)
        return('[Record Updated]')
    except:
        return('[ERROR in fireRTDB_push]')
    