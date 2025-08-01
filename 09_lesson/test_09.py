from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert():
    sql = text("insert into student(user_id,education_form,subject_id) values (1235600, 'group', 1)")
    db.execute(sql)
    user = text("select * from student where user_id= 1235600")
    user_id = db.execute(user).fetchall() 
    assert user_id[0][0] == 1235600
    print(user_id)


def test_update():
    sql = text("update student set level = 'Beginner' where user_id=1235600")
    db.execute(sql)
    user = text("select * from student where user_id= 1235600")
    user_id = db.execute(user).fetchall() 
    assert user_id[0][1] is not None
    assert user_id[0][1] == 'Beginner'
    print(user_id)


def test_delete():
    sql = text("delete from student where user_id=1235600")
    db.execute(sql)
    user = text("select * from student where user_id= 1235600")
    user_id = db.execute(user).fetchall() 
    assert user_id == []
    print(user_id)


        





