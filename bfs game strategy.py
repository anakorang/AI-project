graf =  {'base A':set(['base B','base C','base E']),
         'base B':set(['base A','base D']),
         'base C':set(['base A','base E','base F']),
         'base D':set(['base B','base E','base G','base H']),
         'base E':set(['base D','base G','base L','base F','base C','base A']),
         'base F':set(['base E','base C','base L','base I']),
         'base G':set(['base D','base H','base J','base L','base E']),
         'base H':set(['base J','base D','base G']),
         'base I':set(['base L','base J','base F']),
         'base J':set(['base H','base G','base L','base I','base K','base M']),
         'base K':set(['base J','base M']),
         'base L':set(['base J','base I','base F','base E','base G']),
         'base M':set(['base K','base J'])}
    

def soldier(graf, mulai, menyerang):
    queue = [[mulai]]
    visited = set()

    while queue:     
        jalur_serang = queue.pop(0)
        state = jalur_serang[-1]

        if state == menyerang:
            return jalur_serang
        elif state not in visited:
            for cabang in graf.get(state, []):
                jalur_serang_baru = list(jalur_serang) 
                jalur_serang_baru.append(cabang) 
                queue.append(jalur_serang_baru)
            visited.add(state)

        isi = len(queue)
        if isi == 0:
            print("Tidak dapat melakukan aksi ini")


