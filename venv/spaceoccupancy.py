import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
os.chdir('C:/Users/sedani.ab/PycharmProjects/pythonfirebase/venv')

cred = credentials.Certificate("spaceoccupancy-firebase-adminsdk.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://spaceoccupancy.firebaseio.com/'
})

ref = db.reference('/')
ref.set({
  "data" : {
    "daily" : {
      "nov29" : {
        "mr1" : 75,
        "mr2" : 60,
        "mr3" : 40,
        "mr4" : 20,
        "unit1" : 75,
        "unit2" : 60,
        "unit3" : 40,
        "unit4" : 20
      },
      "nov26" : {
        "mr1" : 60,
        "mr2" : 20,
        "mr3" : 40,
        "mr4" : 75,
        "unit1" : 60,
        "unit2" : 20,
        "unit3" : 40,
        "unit4" : 75
      }
    },
	  "monthly" : {
      "jan" : {
        "mr1" : 75,
        "mr2" : 60,
        "mr3" : 40,
        "mr4" : 20,
        "unit1" : 75,
        "unit2" : 60,
        "unit3" : 40,
        "unit4" : 20
      },
      "feb" : {
        "mr1" : 60,
        "mr2" : 20,
        "mr3" : 40,
        "mr4" : 75,
        "unit1" : 60,
        "unit2" : 20,
        "unit3" : 40,
        "unit4" : 75
      },
	   "dec" : {
        "mr1" : 60,
        "mr2" : 20,
        "mr3" : 40,
        "mr4" : 75,
        "unit1" : 60,
        "unit2" : 20,
        "unit3" : 40,
        "unit4" : 75
      }
    },
	"yearly" : {
      "2017" : {
        "mr1" : 75,
        "mr2" : 60,
        "mr3" : 40,
        "mr4" : 20,
        "unit1" : 75,
        "unit2" : 60,
        "unit3" : 40,
        "unit4" : 20
      },
      "2018" : {
        "mr1" : 60,
        "mr2" : 20,
        "mr3" : 40,
        "mr4" : 75,
        "unit1" : 60,
        "unit2" : 20,
        "unit3" : 40,
        "unit4" : 75
      }
    }
  }
}
)
