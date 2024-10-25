from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
import crud
import model
import schema

# Initialize FastAPI
app = FastAPI()

model.Base.metadata.create_all(bind=engine)

@app.post("/listings/", response_model=schema.Listing, status_code=status.HTTP_201_CREATED)
def create_listing(listing: schema.ListingCreate, db: Session = Depends(get_db)):
    return crud.create_listing(db=db, listing=listing)


@app.get("/listings/{listing_id}", response_model=schema.Listing, status_code=200)
def read_listing(listing_id: int, db: Session = Depends(get_db)):
    listing = crud.get_listing(db, listing_id=listing_id)
    if listing is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return listing


@app.get("/listings/", response_model=list[schema.Listing], status_code=200)
def read_listings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    listings = crud.get_listings(db, skip=skip, limit=limit)
    return listings


@app.delete("/listings/{listing_id}")
def delete_listing(listing_id: int, db: Session = Depends(get_db)):
    crud.delete_listing(db, listing_id=listing_id)
