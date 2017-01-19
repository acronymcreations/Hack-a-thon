# Bug Hunt

### Disclaimer

This is a blog built in python using flask.  It has purposly been built with numerous security holes in order to use
as an educational tool to teach about cyber security. This site should not be used to host any type of real data or be used for any production service.

## Bugs Found

1. The cookie used for authentication was simply 'userID|username'.  Thus, cookies were very easy to forge by guessing another user's ID.

	- Fixed by using MD5 to hash part of the cookie, making it harder to forge.

2. Users were able to access the database and discovered the passwords were being stored in plain text.  Thus, everyone's passwords were compromised.

	- Fixed by storing hashed passwords instead of plain text passwords.  Passwords are hashed using MD5.
