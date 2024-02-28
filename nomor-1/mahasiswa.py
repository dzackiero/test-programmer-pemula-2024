import functools
import sqlite3
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

bp = Blueprint("mahasiswa", __name__, url_prefix="/mahasiswa")


@bp.route("/", methods=["POST"])
def index():
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
