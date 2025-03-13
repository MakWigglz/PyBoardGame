from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os
from dotenv import load_dotenv

load_dotenv()

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Square(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  col: Mapped[int] = mapped_column(Integer)
  row: Mapped[int] = mapped_column(Integer)
  paragraph: Mapped[str] = mapped_column(String)
  visited: Mapped[bool] = mapped_column(Boolean, default=False)

  def __repr__(self):
    return f"<Square(col={self.col}, row={self.row}, paragraph={self.paragraph}, visited={self.visited})>"

def create_default_squares(app):
  with app.app_context():
    for col in range(8):
      for row in range(8):
        new_square = Square(col=col, row=row, paragraph=f"This is the paragraph for square ({col}, {row}).")
        db.session.add(new_square)
    db.session.commit()

def are_all_squares_visited():
  all_visited = True
  for square in Square.query.all():
    if square.visited is False:
      all_visited=False
      break
  return all_visited

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///boardgame.db")
db.init_app(app)

# Create the db if it does not exist
with app.app_context():
    db.create_all()
    if not Square.query.first():
      create_default_squares(app)

@app.route("/get_paragraph/<int:col>/<int:row>", methods=["GET"])
def get_paragraph(col, row):
    # check if the square exist
    square = Square.query.filter_by(col=col, row=row).first()
    if square is None:
      return jsonify({"error": "Square not found"}), 404

    # update square visited status
    square.visited = True
    db.session.commit()

    return jsonify({"paragraph": square.paragraph, "game_over": are_all_squares_visited()})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
