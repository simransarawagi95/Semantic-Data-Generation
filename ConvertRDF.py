import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef, OWL
from rdflib.namespace import XSD

# Define namespaces for the ontology
NS = Namespace("http://example.org/")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("./food_table2.csv")

# Create an RDF graph
g = Graph()

#Define Person Class
g.add((NS.Person, RDF.type, RDFS.Class))
g.add((NS.Person, RDFS.label, Literal("Person", lang="en")))

# Define the Age class with minimum and maximum age values
g.add((NS.Age, RDF.type, RDFS.Class))
g.add((NS.Age, RDFS.label, Literal("Age", lang="en")))
g.add((NS.Age, RDF.type, RDFS.Datatype))
g.add((NS.Age, RDFS.range, RDFS.Literal))
g.add((NS.Age, RDF.type, RDF.Property))

demographics = {"child", "adult", "senior"}

# Define age groups as subclasses of Age with different age ranges
g.add((NS.Child, RDF.type, RDFS.Class))
g.add((NS.Child, RDFS.label, Literal("Child", lang="en")))
g.add((NS.Child, RDFS.subClassOf, NS.Age))
g.add((NS.Child, RDFS.subClassOf, NS.Person))
g.add((NS.Child, RDFS.range, Literal(2, datatype=XSD.integer)))
g.add((NS.Child, RDFS.range, Literal(19, datatype=XSD.integer)))

g.add((NS.Adult, RDF.type, RDFS.Class))
g.add((NS.Adult, RDFS.label, Literal("Adult", lang="en")))
g.add((NS.Adult, RDFS.subClassOf, NS.Age))
g.add((NS.Adult, RDFS.subClassOf, NS.Person))
g.add((NS.Adult, RDFS.range, Literal(20, datatype=XSD.integer)))
g.add((NS.Adult, RDFS.range, Literal(64, datatype=XSD.integer)))

g.add((NS.Senior, RDF.type, RDFS.Class))
g.add((NS.Senior, RDFS.label, Literal("Senior", lang="en")))
g.add((NS.Senior, RDFS.subClassOf, NS.Age))
g.add((NS.Senior, RDFS.subClassOf, NS.Person))
g.add((NS.Senior, RDFS.range, Literal(65, datatype=XSD.integer)))
g.add((NS.Senior, RDFS.range, Literal(100, datatype=XSD.integer)))

#Create Food Group Class
foodgroups = {"AddedSugar", "Discretionaryfats", "Discretionaryoils"}

g.add((NS.FoodGroup, RDF.type, RDFS.Class))
g.add((NS.FoodGroup, RDFS.label, Literal("Food Group", lang="en")))

#Create Types of Food Groups
g.add((NS.AddedSugar, RDF.type, RDFS.Class))
g.add((NS.AddedSugar, RDFS.label, Literal("Added sugar", lang="en")))
g.add((NS.AddedSugar, RDFS.subClassOf, NS.FoodGroup))

g.add((NS.Discretionaryfats, RDF.type, RDFS.Class))
g.add((NS.Discretionaryfats, RDFS.label, Literal("Discretionary fats", lang="en")))
g.add((NS.Discretionaryfats, RDFS.subClassOf, NS.FoodGroup))

g.add((NS.Discretionaryoils , RDF.type, RDFS.Class))
g.add((NS.Discretionaryoils , RDFS.label, Literal("Discretionary oils ", lang="en")))
g.add((NS.Discretionaryoils , RDFS.subClassOf, NS.FoodGroup))

g.add((NS.Dairy, RDF.type, RDFS.Class))
g.add((NS.Dairy, RDFS.label, Literal("Dairy", lang="en")))
g.add((NS.Dairy, RDFS.subClassOf, NS.FoodGroup))

g.add((NS.Fruit, RDF.type, RDFS.Class))
g.add((NS.Fruit, RDFS.label, Literal("Fruit", lang="en")))
g.add((NS.Fruit, RDFS.subClassOf, NS.FoodGroup))

g.add((NS.Vegetables, RDF.type, RDFS.Class))
g.add((NS.Vegetables, RDFS.label, Literal("Vegetables", lang="en")))
g.add((NS.Vegetables, RDFS.subClassOf, NS.FoodGroup))

g.add((NS.Potatoes, RDF.type, RDFS.Class))
g.add((NS.Potatoes, RDFS.label, Literal("Potatoes", lang="en")))
g.add((NS.Potatoes, RDFS.subClassOf, NS.Vegetables))

g.add((NS.Tomatoes, RDF.type, RDFS.Class))
g.add((NS.Tomatoes, RDFS.label, Literal("Tomatoes", lang="en")))
g.add((NS.Tomatoes, RDFS.subClassOf, NS.Vegetables))

g.add((NS.RedOrange, RDF.type, RDFS.Class))
g.add((NS.RedOrange, RDFS.label, Literal("Red & Orange without Tomatoes", lang="en")))
g.add((NS.RedOrange, RDFS.subClassOf, NS.Vegetables))

g.add((NS.DarkGreen, RDF.type, RDFS.Class))
g.add((NS.DarkGreen, RDFS.label, Literal("Dark Green", lang="en")))
g.add((NS.DarkGreen, RDFS.subClassOf, NS.Vegetables))

g.add((NS.Grains, RDF.type, RDFS.Class))
g.add((NS.Grains, RDFS.label, Literal("Grains", lang="en")))
g.add((NS.Grains, RDFS.subClassOf, NS.FoodGroup))

g.add((NS.Refined, RDF.type, RDFS.Class))
g.add((NS.Refined, RDFS.label, Literal("Grains:Refined", lang="en")))
g.add((NS.Refined, RDFS.subClassOf, NS.Grains))

g.add((NS.Whole, RDF.type, RDFS.Class))
g.add((NS.Whole, RDFS.label, Literal("Grains:Whole", lang="en")))
g.add((NS.Whole, RDFS.subClassOf, NS.Grains))

g.add((NS.Protein, RDF.type, RDFS.Class))
g.add((NS.Protein, RDFS.label, Literal("Protein Foods", lang="en")))
g.add((NS.Protein, RDFS.subClassOf, NS.FoodGroup))

#Create Location Class
g.add((NS.AtHome, RDF.type, RDFS.Class))
g.add((NS.AtHome, RDFS.label, Literal("At Home", lang="en")))

g.add((NS.NotAtHome, RDF.type, RDFS.Class))
g.add((NS.NotAtHome, RDFS.label, Literal("Not At Home", lang="en")))

g.add((NS.Restaurant, RDF.type, RDFS.Class))
g.add((NS.Restaurant, RDFS.label, Literal("Restaurant", lang="en")))
g.add((NS.Restaurant, RDFS.subClassOf, NS.NotAtHome))

g.add((NS.Fastfood, RDF.type, RDFS.Class))
g.add((NS.Fastfood, RDFS.label, Literal("Fast food", lang="en")))
g.add((NS.FastFood, RDFS.subClassOf, NS.NotAtHome))

g.add((NS.School, RDF.type, RDFS.Class))
g.add((NS.School, RDFS.label, Literal("School", lang="en")))
g.add((NS.FastFood, RDFS.subClassOf, NS.NotAtHome))

g.add((NS.Other, RDF.type, RDFS.Class))
g.add((NS.Other, RDFS.label, Literal("Other", lang="en")))
g.add((NS.Other, RDFS.subClassOf, NS.NotAtHome))


#Defining Quantity Class
g.add((NS.Quantity, RDF.type, RDFS.Class))
g.add((NS.Quantity, RDFS.label, Literal("Quantity", lang="en")))

#Defining URIs for Relationships
eats = URIRef(f"{NS}eats")
consumed = URIRef(f"{NS}consumedAt")
quantity = URIRef(f"{NS}quantity")

#Defining Custom Relationship between Classes
g.add((eats, RDF.type, OWL.ObjectProperty))
g.add((eats,RDFS.domain,NS.Person))
g.add((eats,RDFS.range,NS.FoodGroup))
g.add((NS.Person,eats,NS.Food))

g.add((consumed, RDF.type, OWL.ObjectProperty))
g.add((consumed,RDFS.domain,NS.FoodGroup))
g.add((consumed,RDFS.range,NS.AtHome))
g.add((consumed,RDFS.range,NS.NotAtHome))
g.add((NS.FoodGroup,consumed,NS.AtHome))
g.add((NS.FoodGroup,consumed,NS.NotAtHome))

g.add((quantity, RDF.type, OWL.ObjectProperty))
g.add((quantity,RDFS.domain,NS.AtHome))
g.add((quantity,RDFS.domain,NS.NotAtHome))



# Iterate over the rows in the DataFrame and create RDF triples for each person
# for i, row in df.iterrows():
#     person_uri = URIRef(f"{NS}person{i}")
#     g.add((person_uri, RDF.type, NS.Person))
#     g.add((person_uri, NS.name, Literal(row['name'])))
#     g.add((person_uri, NS.age, Literal(row['age'], datatype=XSD.integer)))
#     g.add((person_uri, NS.gender, Literal(row['gender'])))

# Serialize the RDF graph to a file in XML format
g.serialize(destination='example.rdf', format='xml')
