"""
data model

"""

import datetime


bulletin_board = []
bno = 1

def save(title : str, content : str, nickname : str)->bool:
    """
    input : title, content, nickname
    output : bool

    내용 저장
    """
    global bno
    date = datetime.datetime.now().date()
    board = {"bno" : bno, "title" : title, "content" : content, "nickname" : nickname, "date" : date, "view_count" : 0}
    bulletin_board.append(board)
    bno+=1
    return True


def list()->list:
    """
    input : x
    output : list[dictionary]

    전체 출력
    """
    return bulletin_board

def read(bno : int)->dict:
    """
    imput : bno
    output : dictionary

    단일 출력
    """
    for board_item in bulletin_board:
        if board_item["bno"] == bno:
            board_item["view_count"] += 1
            return board_item
    return None


def update(bno : int , title : str, content : str)->bool:
    """
    input : bno, title, content
    output : bool

    업데이트
    """
    for board_item in bulletin_board:
        if board_item["bno"] == bno:
            board_item["title"] = title
            board_item["content"] = content
            return True
    return False

def delete(bno : int)->bool:
    """
    input : bno
    output : bool

    삭제
    """
    for board_item in bulletin_board:
        if board_item["bno"] == bno:
            bulletin_board.remove(board_item)
            return True
    return False