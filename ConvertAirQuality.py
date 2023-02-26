import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef, OWL
from rdflib.namespace import XSD
from datetime import datetime

# Define namespaces for the ontology
NS = Namespace("http://example.org/")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("./AirQuality.csv")
header_names = df.columns.tolist()
header_names = [element.strip() for element in header_names]

# Create an RDF graph
g = Graph()

#Define GeoId Class
RowId = URIRef("http://example.org/RowId")
g.add((RowId, RDF.type, OWL.Class))
g.add((NS.PolicyArea,RDF.type,OWL.Class))
g.add((NS.Dataset,RDF.type,OWL.Class))
g.add((NS.Tract,RDF.type,OWL.Class))
for row in header_names:
    if(row=="PolicyArea"):
        g.add((NS.PolicyName,RDF.type,OWL.DatatypeProperty))
    elif(row=="Dataset"):
        g.add((NS.SetName,RDF.type,OWL.DatatypeProperty))
    elif(row=="Tract"):
        g.add((NS.TractName,RDF.type,OWL.DatatypeProperty))
        g.add((NS.TractNo,RDF.type,OWL.DatatypeProperty))
    else:
        g.add((NS.row,RDF.type,OWL.DatatypeProperty))

#Defining Relation between each row and policy,dataset,tract
g.add((NS.hasPolicy, RDF.type, OWL.ObjectProperty))
g.add((NS.hasPolicy, RDFS.domain, NS.RowId))
g.add((NS.hasPolicy, RDFS.range, NS.PolicyArea))

g.add((NS.ofDataSet, RDF.type, OWL.ObjectProperty))
g.add((NS.ofDataSet, RDFS.domain, NS.RowId))
g.add((NS.ofDataSet, RDFS.range, NS.Dataset))

g.add((NS.hasTract, RDF.type, OWL.ObjectProperty))
g.add((NS.hasTract, RDFS.domain, NS.RowId))
g.add((NS.hasTract, RDFS.range, NS.Tract))


#Defining Properties for DataTypeProperty
g.add((NS.Date, RDFS.range, XSD.date))
g.add((NS.Year,RDFS.range,XSD.year))
g.add((NS.Year,RDFS.subClassOf,NS.Date))

# Iterate over the rows in the DataFrame and create RDF triples for each person
for i, row in df.iterrows():
    policy_uri=URIRef(f"{NS}row{row['Policy Area']}")
    g.add((policy_uri, RDF.type, NS.PolicyArea))
    g.add((policy_uri, NS.PolicyName, Literal(row['Policy Area'])))
for i, row in df.iterrows():
    set_name=row['Dataset'].replace(" ","")
    set_uri=URIRef(f"{NS}row{set_name}")
    g.add((set_uri, RDF.type, NS.Dataset))
    g.add((set_uri, NS.SetName, Literal(row['Dataset'])))
for i, row in df.iterrows():
    tract_uri=URIRef(f"{NS}row{row['Tract Number']}")
    g.add((tract_uri, RDF.type, NS.Tract))
    g.add((tract_uri, NS.TractName, Literal(row['Tract'])))
    g.add((tract_uri, NS.TractNo, Literal(row['Tract Number'])))
for i, row in df.iterrows():
        row_uri = URIRef(f"{NS}row{row['Row ID']}")
        g.add((row_uri, RDF.type, NS.RowId))
        # g.add((row_uri, NS.PolicyArea, Literal(row['Policy Area'])))
        # g.add((row_uri, NS.Dataset, Literal(row['Dataset'])))
        g.add((row_uri, NS.Variable, Literal(row['Variable'])))
        g.add((row_uri, NS.Year, Literal(row['Year'], datatype=XSD.year)))
        g.add((row_uri, NS.Count, Literal(row['Count'])))
        #g.add((row_uri, NS.Tract, Literal(row['Tract'])))
        g.add((row_uri, NS.TractNumber, Literal(row['Tract Number'])))
        g.add((row_uri, NS.Neighborhood, Literal(row['Neighborhood'])))
        g.add((row_uri, NS.GEOID, Literal(row['GEOID'])))
        g.add((row_uri, NS.Location, Literal(row['Location'])))
        g.add((row_uri, NS.Date, Literal(datetime.strptime(row['Date'], '%d/%m/%y').date(), datatype=XSD.date)))


# Serialize the RDF graph to a file in XML format
g.serialize(destination='AirQuality.rdf', format='xml')
