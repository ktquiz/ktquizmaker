from flask import Flask


# kind of like a gateway for all stuff in the .ahp package


from werkzeug.security import generate_password_hash, check_password_hash
from random import choice
import string, random, json
import sqlalchemy
from flask import flash
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, scoped_session
from sqlalchemy.pool import StaticPool as SP
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

logged_in = False
sahlt = ''
bgh = 0
boo = ''
f = string.ascii_letters + string.digits + string.punctuation
engine = sqlalchemy.create_engine('sqlite:///hi.sqlite',
                                  connect_args={'check_same_thread': False},
                                  poolclass=SP,
                                  echo=False)
base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))
Session = Session()


class User(base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True)
    name = Column(String)
    salt = Column(Integer)
    password = Column(String)
    scores = Column(String)
    quiz = relationship("quiz")


class quiz(base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    retakable = Column(Boolean)
    randomo = Column(Boolean)
    owner_name = Column(String)
    name = Column(String(collation='NOCASE'))
    scores = Column(String)
    owner_id = Column(Integer, ForeignKey("users.uid"))


class question(base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    correct_answer = Column(String)
    question = Column(String)
    question_type = Column(String)
    question_data = Column(String)
    ammounts = Column(Integer)
    owner_id = Column(Integer, ForeignKey("quiz.id"))


base.metadata.create_all(engine)


def generate_salt(b, salt):
    b = 0
    while b < 500:
        x = list(f)
        q = choice(x)
        salt = salt + str(q)
        b += 1
    return (salt)


def gq(a):
  print(type(a))
  i = Session.query(quiz).filter_by(id=a)
  i = i.first()
  d = i.randomo
  c = Session.query(question).filter_by(owner_id=i.id)
  c = c.all()
  e = [c,d,i]
  return e


def signup(b, c, d):
    """
    b = str(request.form["email"])
    c = str(request.form["pswd"])
    d = str(request.form["pswd2"])
    """
    salt = generate_salt(boo, sahlt)
    d = Session.query(User).filter_by(name=b)
    e = d.first()
    d = Session.query(User).filter_by(name=b)
    d = d.all()
    if len(d) >= 1:
        flash("that name is taken", 'danger')
    else:
        i = generate_password_hash(c + str(salt))
        t = {}
        t = json.dumps(t)
        bob = User(name=b, password=i, salt=salt,scores=t)
        Session.add(bob)
        Session.commit()
        return i


def create_quiz(names, named, retakables, ro):
    d = Session.query(User).filter_by(name=names)
    e = d.first()
    t = {}
    t = json.dumps(t)
    print(e.uid)
    quiz_ = quiz(name=named,
                 owner_id=e.uid,
                 owner_name=e.name,
                 retakable=retakables,
                 randomo=ro,scores=t)
    Session.add(quiz_)
    Session.commit()
    return quiz_


def loginn(b, c):
    d = Session.query(User).filter_by(name=b)
    e = d.first()
    g = d.all()
    if len(g) != 1:
        return 'l'
    d = check_password_hash(e.password, (c + e.salt))

    if d == True:
        flash('success', 'success')

        return (e.name, str(e.password))

    else:
        return 'h'


def add_question(ques, ca, qd, ow_id, qt, amm):
    qu = question(question=ques,
                  correct_answer=ca,
                  question_data=qd,
                  owner_id=ow_id,
                  question_type=qt,
                  ammounts=amm)
    Session.add(qu)
    Session.commit()
    return [
        qu.question, qu.correct_answer, qu.question_data, qu.owner_id,
        qu.question_type, qu.ammounts, qu.id
    ]


def check_if_login(p, n):
    try:
        d = Session.query(User).filter_by(name=n)
        e = d.first()
        print(e.password)
        print(p)
        ff = bool(str(e.password) == p)
        if p == str(e.password):
            return 'success'
    except:
      print('failed')
def get_quiz(qz):
    one = Session.query(quiz).filter_by(name=qz).all()
    two = Session.query(quiz).filter(quiz.name.like(f'{qz}%'
                                                    or f'%{qz}')).all()
    four = Session.query(quiz).filter(quiz.owner_name.like(f'%{qz}%')).all()
    three = Session.query(quiz).filter(quiz.name.like(f'%{qz}%')).all()
    quiz_ = []
    ids = []
    g = 1
    for i in one:
        quiz_.append(i)
        ids.append(i.id)
        g += 1

    g = 1

    for i in two:
        if i.id not in ids:
            quiz_.append(i)
            ids.append(i.id)
            g += 1
    g = 1

    for i in three:
        if i.id not in ids:
            quiz_.append(i)
            ids.append(i.id)
            g += 1
    g = 1

    for i in four:
        if i.id not in ids:
            quiz_.append(i)
            ids.append(i.id)
            g += 1
    return (quiz_)
    
def score(scores,name,score):
  scor = json.loads(scores)
  if name in scor:
    a = scor[name]
    a.append(score)
    scor.update({name:a})
  else:
    s= []
    s.append(score)
    scor[f"{name}"] = list(s)
  scor = json.dumps(scor)
  return scor
def get_user(u):
  a = Session.query(User).filter_by(name=u)
  a = a.first()
  return a
  
def get_data(a):
  a = get_user(a)
  b = Session.query(quiz).filter_by(owner_id=a.uid)
  b=b.all()
  t = []
  for i in b:
    aa = {'score': i.scores, 'name': i.name}
    t.append(aa)
  c = a.scores
  return [c,json.dumps(t)]

