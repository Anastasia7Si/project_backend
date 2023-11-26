from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .database import LocalSession, engine
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()



@app.get('/dealers/{dealer_id}/', response_model=schemas.Dealer)
def get_dealer(dealer_id: int, db: Session = Depends(get_db)):
    db_dealer = crud.get_dealer(db, dealer_id=dealer_id)
    if db_dealer is None:
        raise HTTPException(status_code=404, detail='Not found')
    return db_dealer


@app.post('/dealers/', response_model=schemas.DealerCreate)
def create_dealer(dealer: schemas.DealerCreate, db: Session = Depends(get_db)):
    return crud.create_dealer(db=db, dealer=dealer)
