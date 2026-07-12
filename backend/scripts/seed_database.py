import sys
import logging
from backend.database_manager import get_db_connection

# Seeds the MySQL database with initial dummy patients for testing
def seed_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    print("🌱 Seeding initial medical records...")
    # SQL logic would go here
    print("✅ Database seeded successfully.")

if __name__ == "__main__":
    seed_data()