import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("swarm.json")
firebase_admin.initialize_app(cred)


'''
#uploading to fire base
firestore_db = firestore.client()
firestore_db.collection(u'GUIDANCE').add({'direction': 'R000F000'})
print('uploaded')
'''


# read data
firestore_db = firestore.client()
snapshots = list(firestore_db.collection(u'GUIDANCE').get())
for snapshot in snapshots:
    print(snapshot.to_dict())


'''
#deleting
firestore_db = firestore.client()
firestore_db.collection(u'GUIDANCE_MESSAGES').delete()
print('Deleted')
'''