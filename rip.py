	# La funzione esegue l'algoritmo utilizzando i due parametri sulla
	# tabella di routing locale definita come variabile globale 
def BellmanFord(src,dv):
	# src: il router da cui viene ricevuto il distance vector
	# dv: il distance vector, un dizionario (chiave -> valore) con
	# - chiave = sottorete di destinazione 
	# - valore = metrica
	global rt; # dichiaro globale la routing table
	# Incremento di uno tutte le distanze nel distance vector	
	for dest in dv.keys(): 
		dv[dest]=dv[dest]+1
	# Scansione del distance vector e aggiornamento routing table
	for dest in dv.keys():
		# Se la destinazione e' nota
		if dest in rt.keys():
			# e il prossimo router e' quello da cui ricevo la tabella, 
			# aggiorno il costo
			if rt[dest][0] == src: rt[dest]=[src,dv[dest]]
            # altrimenti, se il costo e' inferiore aggiorno il costo e il router
			elif rt[dest][1] > dv[dest]: 
				rt[dest]=[src,dv[dest]]
        # se invece la destinazione non e' nota aggiungo una nuova riga
		else: rt[dest]=[src,dv[dest]]
	return

# Esempio sugli appunti
# rt = routing table (variabile globale) e' un dizionario (chiave -> valore) con
# - chiave: il nome della sottorete di destinazione
# - valore: la coppia [next-hop,metrica]
rt={
 'n1':['A',1],
 'n2':['C',1],
 'n3':['A',3],
 'n4':['B',1],
 'n5':['B',2]}

BellmanFord('C',{'n2':1,'n3':0,'n6':4})
print(rt)
# qui potete aggiungere altre invocazioni
