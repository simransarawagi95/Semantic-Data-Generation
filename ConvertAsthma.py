import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef, OWL
from rdflib.namespace import XSD

# Define namespaces for the ontology
NS = Namespace("http://example.org/")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("./Asthma.csv")
header_names = df.columns.tolist()
header_names = [element.strip() for element in header_names]

# Create an RDF graph
g = Graph()

#Define GeoId Class
RowId = URIRef("http://example.org/RowId")
g.add((RowId, RDF.type, OWL.Class))
for row in header_names:
    g.add((NS.row,RDF.type,OWL.DatatypeProperty))
# g.add((NS.Tract, RDF.type, OWL.DatatypeProperty))
# g.add((NS.TractNo, RDF.type, OWL.DatatypeProperty))
# g.add((NS.Neighborhood, RDF.type, OWL.DatatypeProperty))
# g.add((NS.Policy, RDF.type, OWL.ObjectProperty))
# Iterate over the rows in the DataFrame and create RDF triples for each person
for i, row in df.iterrows():
     row_uri = URIRef(f"{NS}row{row['Row ID']}")
     g.add((row_uri, RDF.type, NS.RowId))
     g.add((row_uri, NS.PolicyArea, Literal(row['Policy Area'])))
     g.add((row_uri, NS.Dataset, Literal(row['Dataset'])))
     g.add((row_uri, NS.Variable, Literal(row['Variable'])))
     g.add((row_uri, NS.Year, Literal(row['Year'])))
     g.add((row_uri, NS.Count, Literal(row['Count'])))
     g.add((row_uri, NS.Tract, Literal(row['Tract'])))
     g.add((row_uri, NS.TractNumber, Literal(row['Tract Number'])))
     g.add((row_uri, NS.Neighborhood, Literal(row['Neighborhood'])))
     g.add((row_uri, NS.GEOID, Literal(row['GEOID'])))
     g.add((row_uri, NS.Location, Literal(row['Location'])))
     g.add((row_uri, NS.Date, Literal(row['Date'])))


# Serialize the RDF graph to a file in XML format
g.serialize(destination='Asthma.rdf', format='xml')
