data = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(data):
    key_list = data.keys()
    value_list=data.values()

    #valid keys check
    lst1= ["a",'b','c','d','e','f','g','h']
    lst2 = [1,2,3,4,5,6,7,8]
    check_key =[]
    for x in lst2:
        for y in lst1:
            check_key.append(str(x)+y)
        
    for i in key_list:
        if i not in check_key:
            print('Invalid Keys')
            break
        
    #valid value check
    color = ['w','b']

    pieces = ['king','queen','bishop','rook','knight','pawn']
    check_piece_name=[]
    for x in color:
        for y in pieces:
            check_piece_name.append(x+y)
    for i in value_list:
        if i =='':
            continue
        elif i not in check_piece_name:
            print('Invalid Piece Names')
            break

    # value num check
    white_king = 0
    black_king = 0
    white_pieces = 0 
    black_pieces = 0
    white_pawns =0 
    black_pawns = 0
    
    flag = True
    #individual piece value
    for i in check_piece_name:
        if i == 'wking':
            white_king += 1
        if i == 'bking':
            black_king += 1
        if i == 'wpawn':
            white_pawns += 1
        if i == 'bpawn':
            black_pawns += 1
        if i.startswith('w'):
            white_pieces += 1
        if i.startswith('b'):
            black_pieces += 1
    #checking values        
    if white_king!=1:
        flag = False
        print('No White King')
    if black_king!=1:
        flag = False
        print('No Black King')
    if white_pawns>8:
        flag = False
        print('White pawns exceeded')
    if black_pawns>8:
        flag=False
        print('Black pawns exceeded')
    if white_pieces>16:
        flag = False
        print('White pieces exceeded')
    if black_pieces>16:
        flag = False
        print('Black pieces exceeded')
    
    #output result
    if flag:
        return True
    else:
        return False

print(isValidChessBoard(data))