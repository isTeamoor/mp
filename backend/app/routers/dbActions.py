from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import FileResponse
from .. import models
from ..database import DB
from pathlib import Path
import os

UPLOAD_DIR = Path() / 'uploaded_images'

DB.createTable()



router = APIRouter(
    prefix="/db",
    tags=['DataBase Actions']
)


@router.post('/createNewAd')
async def createNewAd(label: str=Form(...), textContent: str=Form(...), img:UploadFile=Form(...)):
    newRecord = DB.query('set', f'''INSERT INTO ads (label, textContent) VALUES ('{label}', '{textContent}')''')
    print(newRecord)

    data = await img.read()
    save_to = UPLOAD_DIR / f"{newRecord}.jpg"
    with open(save_to, 'wb') as f:
        f.write(data)
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
    os.remove(UPLOAD_DIR / f"{deletedAd.id}.jpg")
    adsList = DB.query('get', '''SELECT * FROM ads''')
    response = []
    for ad in adsList:
        response.append({
            'id':ad[0], 'label':ad[1], 'textContent':ad[2]
        })
    return response



@router.get('/getImg/{imgID}')
def uploadIMG(imgID:int):
    return FileResponse(UPLOAD_DIR / f"{imgID}.jpg")

