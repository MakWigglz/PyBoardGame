# setup_database.py
class SimpleDatabase:
    def __init__(self):
        self.data = {}
    def insert(self, key, value):
        self.data[key] = value
    def fetch(self, key):
        return self.data.get(key)
    def display_all(self):
        return self.data.items()
# Example usage
if __name__ == "__main__":
    db = SimpleDatabase()
    
    # Insert topics with multiple paragraphs
    db.insert("square_1", {
        "color": "red",
        "subject": "Math",
        "paragraphs": [
            "Math is the study of numbers, shapes, and patterns.",
            "Algebra is one of the main branches of mathematics.",
            "Geometry deals with the properties and relations of points, lines, surfaces, and solids."
        ]
    })
    db.insert("square_2", {
        "color": "blue",
        "subject": "Science",
        "paragraphs": [
            "Science is the systematic study of the structure and behavior of the physical and natural world.",
            "Physics, chemistry, and biology are the main branches of science.",
            "Scientific methods involve observation, experimentation, and analysis."
        ]
    })
    # Add more squares as needed...
    print(db.display_all())