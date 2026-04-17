# add.py

from folder import EndeeVectorDB

# 🔹 Initialize DB
db = EndeeVectorDB()

# 🔹 Load text file
def load_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()

# 🔹 Clean text (optional)
def clean_text(lines):
    return [line.strip() for line in lines if line.strip() != ""]

# 🔹 Add data to DB
def add_data(file_path):
    print("📂 Loading file...")
    lines = load_text_file(file_path)

    print("🧹 Cleaning text...")
    docs = clean_text(lines)

    print("⚡ Adding to vector DB...")
    db.add_documents(docs)

    print("✅ Data successfully added!")

# 🔹 Run script
if __name__ == "__main__":
    file_path = "data/sample.txt"   # change path if needed
    add_data(file_path)
