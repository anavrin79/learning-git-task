articles_dict = {
    "Warzywniak": ["Marchew", "Seler", "Rukola"],
    "Piekarnia": ["Chleb", "Pączek", "Bułki"]
}

sumofelements=0

print("Lista zakupów")

for i in articles_dict:
    print ("Idę do ", i , "po :" , articles_dict[i])
    sumofelements += len(articles_dict[i])

print ("W sumie kupuję ", sumofelements, "produktów.")