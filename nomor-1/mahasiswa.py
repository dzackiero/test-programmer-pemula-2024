import sqlite3
from flask import Blueprint, request, jsonify

from db import get_db

bp = Blueprint("mahasiswa", __name__, url_prefix="/mahasiswa")


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        search = request.args.get("search")
        db = get_db()
        try:
            if search != None:
                query = "SELECT * FROM Mahasiswa WHERE name %?%"
                cursor = db.execute(query, (search))
            else:
                query = "SELECT * FROM Mahasiswa"
                cursor = db.execute(query)
            rows = cursor.fetchall()
            students = []
            for i in rows:
                student = {}
                student["NIM"] = i["NIM"]
                student["NamaLengkap"] = i["NamaLengkap"]
                student["Jurusan"] = i["Jurusan"]
                students.append(student)
            return jsonify(
                {"status": 200, "message": "success", "data": students},
                200,
            )
        except sqlite3.Error as e:
            return jsonify(
                {
                    "status": 500,
                    "message": "Failed to insert data into the database",
                    "error": str(e),
                },
                500,
            )
    else:
        nim = request.form["nim"]
        name = request.form["nama"]
        major = request.form["jurusan"]

        db = get_db()
        try:
            db.execute(
                "INSERT INTO Mahasiswa(NIM, NamaLengkap, Jurusan) VALUES (?, ?, ?)",
                (nim, name, major),
            )
            db.commit()
            return jsonify(
                {
                    "status": 200,
                    "message": "success",
                    "data": {"nim": nim, "NamaLengkap": name, "major": major},
                },
                200,
            )
        except sqlite3.Error as e:
            return jsonify(
                {
                    "status": 500,
                    "message": "Failed to insert data into the database",
                    "error": str(e),
                },
                500,
            )


@bp.route("/<int:nim>", methods=["PUT"])
def edit(nim):
    name = request.form["nama"]
    major = request.form["jurusan"]

    db = get_db()
    try:
        db.execute(
            "UPDATE Mahasiswa SET NamaLengkap = ?, Jurusan = ? WHERE NIM == ?",
            (name, major, nim),
        )
        db.commit()
        return jsonify(
            {
                "status": 200,
                "message": "success",
                "data": {"nim": nim, "NamaLengkap": name, "major": major},
            },
            200,
        )
    except sqlite3.Error as e:
        return jsonify(
            {
                "status": 500,
                "message": "Failed to insert data into the database",
                "error": str(e),
            },
            500,
        )
