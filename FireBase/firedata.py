def fireData(direction,id):
    try:

        import firebase_admin
        from firebase_admin import credentials, firestore
        cred = credentials.Certificate("FireBase/swarm.json")
        firebase_admin.initialize_app(cred)

        firestore_db = firestore.client()
        firestore_db.collection(u'GUIDANCE').document(str(id)).set({'direction': 'R002F010'})
        return('[uploaded to cloud]')
    except:
        return('[ERROR in fireData]')

