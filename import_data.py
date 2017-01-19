from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Post

engine = create_engine('sqlite:///hack.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

po = session.query(Post).delete()
print 'deleted %s rows from Post' % po
session.commit()

us = session.query(User).delete()
print 'deleted %s rows from User' % us
session.commit()

newuser = User(name='Marissa Mayer',email='yahoo@yahoo.com',username='MMayer',password='46ea0d5b246d2841744c26f72a86fc29')
newuser2 = User(name='M Wright',email='mgwright@episd.org',username='mgwright',password='e99a18c428cb38d5f260853678922e03')
session.add(newuser)
session.add(newuser2)
session.commit()

newpost = Post(title='Edit this Post!',desc='Add your name to this post or delete it all together.',user_id=1)
session.add(newpost)
session.commit()