from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/emails/create/')
def emails_create():
    name = request.args['name']
    emails = request.args['emails']

    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = f'''
        INSERT INTO emails (name, emails)
        VALUES ('{name}', '{emails}');
        '''

    cur.execute(sql)
    con.commit()
    con.close()
    return 'ok'


@app.route('/emails/reade/')
def emails_reade():
    id_new = request.args.get('id')

    con = sqlite3.connect('example.db')
    cur = con.cursor()

    if id_new:
        sql = f'''SELECT * FROM emails WHERE id={id_new};'''
    else:
        sql = f'''SELECT * FROM emails ORDER BY name ASC;'''

    cur.execute(sql)
    results = cur.fetchall()
    con.close()
    return str(results)


@app.route('/emails/update/')
def emails_update():
    id_new = request.args['id']
    name = request.args['name']

    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = f'''UPDATE emails SET name='{name}' WHERE id={id_new};'''

    cur.execute(sql)
    con.commit()
    con.close()
    return 'OK'


@app.route('/emails/delete/')
def emails_delete():
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = f'''DELETE FROM emails;'''

    cur.execute(sql)
    con.commit()
    con.close()
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
