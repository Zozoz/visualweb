from django.shortcuts import render
import sqlite3


def show(request):
    conn = sqlite3.connect('poj/recommend.db')
    cur = conn.cursor()
    sql = "select * from recommend limit 100"
    cur.execute(sql)
    data = cur.fetchall()
    username = []
    for item in data:
        username.append(item[1])
    return render(request, 'poj/show.html',
            {
                'username': username,
            }
    )


def detail(request, username):
    print username
    conn = sqlite3.connect('poj/recommend.db')
    cur = conn.cursor()
    sql = "select * from recommend where username = ?"
    cur.execute(sql, (username,))
    problem = cur.fetchone()[2]
    print sql
    print problem
    return render(request, 'poj/detail.html',
            {
                'problem': problem,
                'username': username,
            }
    )
