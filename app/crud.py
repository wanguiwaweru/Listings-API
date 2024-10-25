from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Response, status
import model
import schema


def get_listing(db: Session, listing_id: int):
    return db.query(models.Listing).filter(models.Listing.id == listing_id).first()


def get_listings(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model.Listing).offset(skip).limit(limit).all()


def create_listing(db: Session, listing: schema.ListingCreate):
    listing = model.Listing(
        name=listing.name, address=listing.address, size=listing.size)
    db.add(listing)
    db.commit()
    db.refresh(listing)
    return listing


def delete_listing(db: Session, listing_id: int):
    listing = db.query(model.Listing).filter(
        models.Listing.id == listing_id).first()
    if not listing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db.delete(listing)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
