hora1 = input("Informe o hora: ")
hora2 = input("Informe a hora: ")
(h1, m1, s1) = hora1.split(":")
(h2, m2, s2) = hora2.split(":")

if int(h1) > 24 or int(h2) > 24 or int(m1) > 60 or int(m2) > 60 or int(s1) > 60 or int(s2) > 60:
    print("Digite corretamente")
else:
    seg = ((int(h1)*3600)+(int(h2) * 3600) + (int(m1)*60)+(int(m2) * 60) + int(s1)+int(s2))
    if seg > 86400:
        seg = seg-86400
    hora = seg/3600
    mins = (seg % 3600)/60
    segs = (seg % 3600) % 60
    hora = int(hora)
    mins = int(mins)
    segs = int(segs)
    print("{}:{}:{}".format(hora, mins, segs))