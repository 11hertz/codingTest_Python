def solution(id_pw, db):
    answer = ''
    
    for user_id, user_pw in db :
        db_id, db_pw = id_pw
        if db_id == user_id and db_pw == user_pw : return 'login'
        if db_id == user_id and db_pw != user_pw : return 'wrong pw'
    
    return 'fail'
