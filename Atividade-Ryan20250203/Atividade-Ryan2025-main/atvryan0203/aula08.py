def resolver_labirinto(lab, x, y, caminho):
    if x < 0 or y < 0 or x >= len(lab) or y >= len(lab[0]) or lab[x][y] == 1:
        return False
    if (x, y) == (len(lab)-1, len(lab[0])-1):
        caminho.append((x,y))
        return True
    lab[x][y] = 1
    caminho.append((x,y))
    if (resolver_labirinto(lab, x+1, y, caminho) or
        resolver_labirinto(lab, x, y+1, caminho) or
        resolver_labirinto(lab, x-1, y, caminho) or
        resolver_labirinto(lab, x, y-1, caminho)):
        return True
    caminho.pop()
    return False

labirinto = [[0,0,1],[1,0,1],[1,0,0]]
caminho = []
resolver_labirinto(labirinto, 0, 0, caminho)
print(caminho) 
