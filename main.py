from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, TEXT, select


#engine = create_engine("mysql+pymysql://root:Flighter099@localhost:3306/test",encoding="utf-8", echo=True)
# metadata = MetaData()

# holo = Table('holosql', metadata,
# Column('Id', TEXT, primary_key=True),
# Column('本名', TEXT),
# Column('別號', TEXT),
# Column('髮色', TEXT),
# Column('瞳色', TEXT),
# Column('身高', Integer),
# Column('年齡', TEXT),
# Column('生日', TEXT),
# Column('屬性', TEXT),
# Column('出身地區', TEXT),
# Column('初配信', TEXT)
# )
# conn = engine.connect()
app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Flighter099@localhost:3306/test"
app.secret_key='any random string'
db.init_app(app)

@app.route("/")
def index():


    return render_template("index.html")

@app.route('/', methods=['POST'])
def result():
     if request.method == 'POST':
         user = request.form.getlist('holo')
         user=str(user).split(',')[0:4]
         session['username'] = user
         return redirect(url_for('test'))


@app.route('/second', methods=['GET','POST'])
def test():
    holoid=session['username']
    # s = select([holo]).where(holo.c.Id.like('aki'))
    # all_users = holo.query.filter_by(Id='aki').all()

    sql = """
        select * from holosql where Id = "aki"
    """
    #
    # query_data = db.engine.execute(sql_cmd)
    #
    # print(db.engine.execute(query_data).fetchone())
    print(holoid[1])
    print(db.engine.execute(sql).fetchall())
    return render_template('second.html')


if __name__ == "__main__":
    app.run(debug=True)