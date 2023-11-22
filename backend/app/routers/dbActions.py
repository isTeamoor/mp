from fastapi import APIRouter
from .. import models
from ..database import DB

DB.createTable()



router = APIRouter(
    prefix="/db",
    tags=['DataBase Actions']
)


@router.post('/createNewAd')
def createNewAd(newAd:models.newCreatedAd):
    DB.query('set', f'''INSERT INTO ads (label, textContent) VALUES ('{newAd.label}', '{newAd.textContent}')''')
    print(DB.query('get', '''SELECT * FROM ads'''))
    return {'working':'yes'}

@router.get('/getAllAds')
def getAllAds():
    adsList = DB.query('get', '''SELECT * FROM ads''')
    response = []
    for ad in adsList:
        response.append({
            'id':ad[0], 'label':ad[1], 'textContent':ad[2]
        })
    print(response)
    return response

@router.post('/deleteAd')
def deleteAd(deletedAd:models.deletedAd):
    DB.query('set', f'''DELETE FROM ads WHERE id = "{deletedAd.id}"''')
    adsList = DB.query('get', '''SELECT * FROM ads''')
    response = []
    for ad in adsList:
        response.append({
            'id':ad[0], 'label':ad[1], 'textContent':ad[2]
        })
    print(response)
    return response
