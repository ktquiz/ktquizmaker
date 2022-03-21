from flask import Blueprint, render_template, request, flash, url_for, make_response
import json
from flask import session as sssession
from random import shuffle, choice
from . import create_quiz, add_question, get_quiz, gq, score, Session, check_if_login, get_user,get_data

quiz = Blueprint('quiz', __name__, template_folder='templates')


@quiz.route('/create', methods=["POST", 'GET'])
def create():
  try:
    check = check_if_login(sssession['password'],sssession['name'])
  except:
    check = ''
  print(check)
  if check == 'success':
    if request.method == "POST":
        b = request.form
        b = dict(b)
        random_unrep = b.values()
        for i in random_unrep:
          if ',' in i:
            flash('you cannot use any commas', 'danger')
            return render_template('create.html',b=True)
        print(b)
        g = str(sssession['name'])
        if b['Retakable'] == 'yes':
            l = True
        else:
            l = False
        if b['Random-order'] == 'yes':
            ll = True
        else:
            ll = False
        q = create_quiz(g, b['quiz name'], l, ll)
        amm = 1
        #qu = question(question=q,correct_answer=ca,question_data= qs,owner_id=quiz_.id,question_type=qt,ammounts=worth)
        x = True
        while x == True:
            if f"quantity_{amm}" in b:
                if b[f'type_{amm}'] == 'Free response':
                    qd = b[f'question_answer_fr_{amm}']
                    ca = b[f'question_answer_fr_{amm}']
                if b[f'type_{amm}'] == 'Multiple choice':
                    qd = []
                    if b[f'mc1_{amm}'] != '' or ' ':
                        qd.append(b[f'mc1_{amm}'.strip()])
                    if b[f'mc2_{amm}'] != '' or ' ':
                        qd.append(b[f'mc2_{amm}'.strip()])
                    if b[f'mc3_{amm}'] != '' or ' ':
                        qd.append(b[f'mc3_{amm}'.strip()])
                    if b[f'mc4_{amm}'] != '' or ' ':
                        qd.append(b[f'mc4_{amm}'.strip()])
                    if b[f'mc5_{amm}'] != '' or ' ':
                        qd.append(b[f'mc5_{amm}'.strip()])
                    if b[f'mc6_{amm}'] != '' or ' ':
                        qd.append(b[f'mc6_{amm}'.strip()])
                    qd = [i for i in qd if i != '']
                    qd = json.dumps(qd)
                    ca = b[f'question_answer_fr_{amm}']
                if b[f'type_{amm}'] == 'True/False':
                    qd = str(b[f't/f_{amm}'])
                    if qd != 'False':
                        print('t')
                        qd = 'False'
                        ca = 'True'
                    else:
                        qd = 'True'
                        ca = 'False'
                f = add_question(b[f'question_name{amm}'],ca, qd, q.id,b[f'type_{amm}'], str(b[f'ammount_of_{amm}']))
                amm += 1
                print(f)
            else:
                x = False
        return render_template('success.html', b=True, x=sssession['name'])

    return render_template('create.html', b=True)


'''
class question(base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    correct_answer = Column(String)
    question = Column(String)
    question_type = Column(String)
    question_data = Column(String)
    ammounts = Column(Integer)
    owner_id = Column(Integer, ForeignKey("quiz.id"))

[['what is 1+1', 'mc', ['3','4','17','42','42','42'], '2','1'], ['is it true', 't/f', true,'2'], ['why', 'fr', 'why not','3']]
'''


@quiz.route('/quihz/<a>', methods=["POST","GET"])
def quihz(a):
  try:
    check = check_if_login(sssession['password'],sssession['name'])
  except:
    check = ''
  if check == 'success':
    a = json.loads(a)
    b = gq(a)
    tt = b[2]
    if tt.retakable == False:
        ttt = json.dumps(tt.scores)
        if sssession['name'] in ttt:
            flash('you cannot retake that quiz', 'danger')
            return render_template('success.html', b=True, x=sssession['name'])
    if request.method == "POST":
        e = request.form
        e = dict(e)
        print(e)
        f = e.keys()
        s = 0
        am = 0
        b=b[0]
        for i in b:
            print(i.correct_answer)
            ggg = e[str(i.id)]
            if i.correct_answer == ggg.strip():
                s += int(i.ammounts)
            am += int(i.ammounts)
            fs = s / am
        fs = round(fs, 5)*100
        tt.scores = score(tt.scores, str(sssession['name']), fs)
        print(a)
        us = get_user(sssession['name'])
        print(us)
        us.scores = score(us.scores, f"{tt.name} by {tt.owner_name}", fs)
        Session.commit()
        return render_template('score.html', b=True, scores=fs)

    return render_template('quiz.html',
                           name=tt.name,
                           owner=tt.owner_name,
                           q=a)


@quiz.route('/quihz/getjson2/<b>', methods=["GET"])
def getjson2(b):
    print('called')
    b = gq(b)
    print(b)
    questions = []
    questions_mc = []
    questions_mc1 = []
    d = b[1]
    b = b[0]
    generic = [
        'yes', 'no', 'sometimes', 'maybe', '42', 'square root of 42',
        'why not', 'occassionally', 'none of the above', 'wood', 'stone',
        'mincraft', 'hi my favorite thing', 'no'
    ]

    for i in b:
        if i.question_type == 'Free response':
            questions.append([i.question, i.question_type, i.id])
        if i.question_type == 'True/False':
            questions.append([i.question, i.question_type, i.id])
        if i.question_type == 'Multiple choice':
            questions.append([i.question, i.question_type, i.id,i.correct_answer])
            questions_mc1.append(i.correct_answer)
            generic.extend(json.loads(i.question_data))

    if d == True:
        shuffle(questions)

    questions_mc = {}
    for i in questions:
      if i[1] == 'Multiple choice':
        q = []
        q.append(i[3])
        while len(q) < 7:
          x = choice(generic)
          if x not in q or questions_mc1:
            q.append(x)
        shuffle(q)
        questions_mc[i[2]]=q
        i[3]='' 
    b=json.dumps({'questions':questions,'questions_mc':questions_mc})
    return b
  
@quiz.route('/search', methods=["POST"])
def search():
  try:
    check = check_if_login(sssession['password'],sssession['name'])
  except:
    check = ''
  if check == 'success':
    qz = request.form['search']

    return render_template('search.html', e=qz)

@quiz.route('/getjson3/<qz>', methods=["POST", "GET"])
def getjson3(qz):
    q = get_quiz(qz)
    qu = []
    for i in q:
        qu.append([i.name, i.owner_name,i.id])
    qu = json.dumps(qu)
    return qu
  
@quiz.route('/getjson', methods=["POST", "GET"])
def getjson():
  g = get_data(sssession['name'])
  return g[0]
  
@quiz.route('/getjson1', methods=["POST", "GET"])
def getjson1():
  g = get_data(sssession['name'])
  return g[1]
    
@quiz.route('/take', methods=["POST", "GET"])
def take():
  try:
    check =      check_if_login(sssession['password'],sssession['name'])
  except:
    check = ''
  print(check)
  if check == 'success':
    return render_template('take.html')
