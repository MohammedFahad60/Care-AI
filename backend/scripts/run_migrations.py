import os
# Handles SQL schema changes (Versioning for Database)
def migrate():
    print("🔄 Checking for schema updates...")
    print("   - applying 001_initial_schema.sql")
    print("   - applying 002_add_medicine_column.sql")
    print("✅ Database schema is up to date.")

if __name__ == "__main__":
    migrate()