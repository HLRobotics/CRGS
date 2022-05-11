
def fireFetch():
    
    try:
        import firebase_admin
        from firebase_admin import credentials, firestore
        cred = credentials.Certificate("FireBase/swarm.json")
        firebase_admin.initialize_app(cred)

        usabledata=[]

        firestore_db = firestore.client()
        snapshots = list(firestore_db.collection(u'GUIDANCE').get())
        for snapshot in snapshots:
            data=snapshot.to_dict()
            a=data['direction']
            usabledata.append(str(a))
        print(usabledata)
        pos=len(usabledata)
        if(usabledata[pos-1]!=usabledata[pos-2]):
            return(usabledata[pos-1])
        else:
            print("[no change]")

    except:
        print('[ERROR IN FIRE FETCH]')
