from app import init
from app.db import init_db


if __name__ == "__main__":
    init_db()
    app = init()

    app.run(debug=True, port=5000)