from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
engine = create_engine(db_connection_string)

Session = sessionmaker(bind=engine)
session = Session()

def clean():
    delete_sql = text("DELETE FROM student WHERE user_id = :user_id").bindparams(user_id=1235600)
    session.execute(delete_sql)
    session.commit()

clean()

def test_insert():
    insert_sql = text("INSERT INTO student(user_id, education_form, subject_id) VALUES(:user_id, :education_form, :subject_id)")\
                        .bindparams(user_id=1235600, education_form='group', subject_id=1)
    session.execute(insert_sql)
    session.commit()
    select_sql = text("SELECT * FROM student WHERE user_id = :user_id").bindparams(user_id=1235600)
    result = session.execute(select_sql).fetchall()
    assert result[0].user_id == 1235600
    print(result)

def test_update():
    update_sql = text("UPDATE student SET level = :level WHERE user_id = :user_id").bindparams(level="Beginner", user_id=1235600)
    session.execute(update_sql)
    
    select_sql = text("SELECT * FROM student WHERE user_id = :user_id").bindparams(user_id=1235600)
    result = session.execute(select_sql).fetchall()
    assert result[0][1] == 'Beginner'
    print(result)

def test_delete():
    delete_sql = text("DELETE FROM student WHERE user_id = :user_id").bindparams(user_id=1235600)
    session.execute(delete_sql)
    session.commit()
    
    select_sql = text("SELECT * FROM student WHERE user_id = :user_id").bindparams(user_id=1235600)
    result = session.execute(select_sql).fetchall()
    assert result == []
    print(result)
