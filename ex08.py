medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
am = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {:.0f}m corresponde a \n{}km \n{}hm \n{}am \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'. format(medida, km, hm, am, dm, cm, mm))
#d = float(input('Digite uma distancia em metros: '))
#print(f'A medida de {d}m corresponde a \n{d*1000:.0f}mm \n{d*100:.0f}cm \n{d*10:.0f}dm \n{d/10:.1f}dam \n{d/100:.2f}hm \n{d/1000:.3f}km.')