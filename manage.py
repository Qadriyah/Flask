from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db
from config import app_settings

app.config.from_object(app_settings["development"])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
