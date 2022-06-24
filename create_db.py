from App import db, create_app, models
# from werkzeug.security import generate_password_hash
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.

# admin_role = models.Role(name='Admin')
# db.session.commit()
# standard_role = models.Role(name='Standard')
# db.session.commit()

# # Create 'user007' user with 'secret' and 'agent' roles
# user1 = models.User(
#     username='user007', email='admin@example.com', active=True,
#     password=generate_password_hash('Password1'))
# user1.roles = [admin_role,]
# db.session.commit()

# # Create a standard user
# user2 = models.User(
#     username='UserStandard', email='standard@example.com', active=True,
#     password=generate_password_hash('Password1'))
# user2.roles = [standard_role,]
# db.session.commit()