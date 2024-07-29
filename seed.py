from app import app, db
from models import Pet
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def drop_database():
    logging.info('Dropping existing database...')
    with app.app_context():
        db.reflect()  # Reflect the existing database schema
        db.drop_all()
        db.session.commit()  # Commit the drop_all operation
    logging.info('Database dropped successfully.')

def seed_database():
    # Drop the existing Database
    drop_database()
    
    # Create all tables
    logging.info('Creating tables...')
    with app.app_context():
        db.create_all()
    logging.info('Tables created successfully.')

    # Add pets data
    logging.info('Adding pets data...')
    with app.app_context():
        fluffy = Pet(name='Saay', age=3, species='Cat', photo_url="https://th.bing.com/th/id/R.686f5c2ea02c48f13471efe9ba24ea3b?rik=3%2bV57gmXjhklrQ&riu=http%3a%2f%2f4.bp.blogspot.com%2f-0b4n4eH5pLo%2fUAWk3E9LXuI%2fAAAAAAAAFf4%2fakYNWAYfqXI%2fs1600%2fYellow%2bEyes%2bcat%2bWallpapers%2b2.jpg&ehk=qITblxFOQKsnSgd0zsIR2i3iqJpixk749MdtM3EPsHk%3d&risl=&pid=ImgRaw&r=0", notes='Saay with cute eye.', available=True)
        rex = Pet(name='Jack', age=5, species='Dog', photo_url="https://th.bing.com/th/id/OIP.Ml9A9gnpLKQA-rEp4N8W9AHaE8?w=272&h=181&c=7&r=0&o=5&pid=1.7", notes='Jack loves  playing.', available=True)
        spike = Pet(name='Bunny', age=2, species='Rabbit', photo_url="https://www.bing.com/th?id=OIP.KFlez8w0LJs8HQIZYZntAgHaLL&w=146&h=221&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2", notes='Spike likes to hide shiny objects.', available=True)
        pets = [fluffy, rex, spike]

        for pet in pets:
            db.session.add(pet)
        db.session.commit()
    logging.info('Pets data added successfully.')

if __name__ == '__main__':
    # Seed the database
    seed_database()
    logging.info('Database seeding completed.')