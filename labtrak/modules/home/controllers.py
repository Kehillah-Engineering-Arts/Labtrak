from labtrak import models

def authenticate_user(username, password):
    """
    Authenticate and return user document from
    database, None on failed auth.  Prepare for
    use as session data.
    """
    user = models.User.auth(username, password)
    if not user:
        return
    user['_id'] = str(user['_id']) # For session data
    return user


def signup(username, email, password, password2, firstname, lastname):
    """Register the user, return error or None."""
    if not (email and '@' in email and '.' in email):
        error = 'You have to enter a valid email address'
    elif models.User.match(username=username):
        error = 'This username is already in use'
    elif models.User.match(email=email):
        error = 'This email is already in use'
    elif not password:
        error = 'You have to enter a password'
    elif password != password2:
        error = 'The passwords do not match'
    else:
        # Insert user into database.
        models.User.create(
            username,
            email,
            password,
            firstname,
            lastname
        )
        return
    return error
