import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef, OWL
from rdflib.namespace import XSD
from datetime import datetime

# Define namespaces for the ontology
NS = Namespace("http://example.org/")

# Read the CSV file into a pandas DataFrame
df1= pd.read_csv("./AirQuality.csv")
df1['Date']=pd.to_datetime(df1['Date'])
df2 = pd.read_csv("./Asthma_LA.csv")
df2['Date']=pd.to_datetime(df2['Date'])

df=pd.merge(df1, df2, on=['Tract Number','Date'], how="inner")


# Create an RDF graph
g = Graph()

#Define Geography Location Class
g.add((NS.County, RDF.type, OWL.Class))
g.add((NS.Neighborhood, RDF.type, OWL.Class))
g.add((NS.Tract, RDF.type, OWL.Class))

#Define Pollutant Variable Class
g.add((NS.Pollutant, RDF.type, OWL.Class))

#Define Air Quality Classes
# g.add((NS.AQI, RDF.type, OWL.Class))
g.add((NS.AQCategory, RDF.type, OWL.Class))

#Define Medical Conditions
g.add((NS.HealthAffect, RDF.type, OWL.Class))

#Define Health Outcome Class
g.add((NS.HealthOutcome, RDF.type, OWL.Class))

#Define Policy Area
g.add((NS.PolicyArea, RDF.type, OWL.Class))

#Define Data Type Properties for Tract Class
g.add((NS.hasName,RDF.type,OWL.DatatypeProperty))
g.add((NS.hasName, RDFS.domain, NS.Tract))
g.add((NS.hasName, RDFS.range, XSD.string))
g.add((NS.hasGeoID,RDF.type,OWL.DatatypeProperty))
g.add((NS.hasGeoID, RDFS.domain, NS.Tract))
g.add((NS.hasGeoID, RDFS.range, XSD.string))
g.add((NS.hasLongitude,RDF.type,OWL.DatatypeProperty))
g.add((NS.hasLongitude, RDFS.domain, NS.Tract))
g.add((NS.hasLongitude, RDFS.range, XSD.float))
g.add((NS.hasLatitude,RDF.type,OWL.DatatypeProperty))
g.add((NS.hasLatitude, RDFS.domain, NS.Tract))
g.add((NS.hasLatitude, RDFS.range, XSD.float))

#Define Data Type Properties for Health Outcome
g.add((NS.hasDate,RDF.type,OWL.DatatypeProperty))
g.add((NS.hasDate, RDFS.domain, NS.HealthOutcome))
g.add((NS.hasDate, RDFS.range, XSD.dateTime))

g.add((NS.hasAQI,RDF.type,OWL.DatatypeProperty))
g.add((NS.hasAQI, RDFS.domain, NS.HealthOutcome))
g.add((NS.hasAQI, RDFS.range, XSD.float))

g.add((NS.hasERVisit,RDF.type,OWL.DatatypeProperty))
g.add((NS.hasERVisit, RDFS.domain, NS.HealthOutcome))
g.add((NS.hasERVisit, RDFS.range, XSD.float))

#Define Data Type Properties for AQ Category
g.add((NS.hasminValue,RDF.type,OWL.DatatypeProperty))
g.add((NS.hasminValue, RDFS.domain, NS.AQCategory))
g.add((NS.hasminValue, RDFS.range, XSD.integer))

g.add((NS.hasmaxValue,RDF.type,OWL.DatatypeProperty))
g.add((NS.hasmaxValue, RDFS.domain, NS.AQCategory))
g.add((NS.hasmaxValue, RDFS.range, XSD.integer))

#Define Relation between Classes using Object Type Property
g.add((NS.isPartof, RDF.type, OWL.ObjectProperty))
g.add((NS.isPartof, RDFS.domain, NS.Neighborhood))
g.add((NS.isPartof, RDFS.range, NS.County))

g.add((NS.hasTract, RDF.type, OWL.ObjectProperty))
g.add((NS.hasTract, RDFS.domain, NS.Neighborhood))
g.add((NS.hasTract, RDFS.range, NS.Tract))

g.add((NS.affects, RDF.type, OWL.ObjectProperty))
g.add((NS.affects, RDFS.domain, NS.Pollutant))
g.add((NS.affects, RDFS.range, NS.Neighborhood))

g.add((NS.hasHealthAffect, RDF.type, OWL.ObjectProperty))
g.add((NS.hasHealthAffect, RDFS.domain, NS.Pollutant))
g.add((NS.hasHealthAffect, RDFS.range, NS.HealthAffect))

g.add((NS.ofTract, RDF.type, OWL.ObjectProperty))
g.add((NS.ofTract, RDFS.domain, NS.HealthOutcome))
g.add((NS.ofTract, RDFS.range, NS.Tract))

# g.add((NS.hasCategory, RDF.type, OWL.ObjectProperty))
# g.add((NS.hasCategory, RDFS.domain, NS.AQI))
# g.add((NS.hasCategory, RDFS.range, NS.AQCategory))

#Define SubClass for AQ Categories
g.add((NS.Good,RDF.type,OWL.Class))
g.add((NS.Good,RDFS.subClassOf,NS.AQCategory))
g.add((NS.Moderate,RDF.type,OWL.Class))
g.add((NS.Moderate,RDFS.subClassOf,NS.AQCategory))
g.add((NS.UnhealthyforSensitiveGroup,RDF.type,OWL.Class))
g.add((NS.UnhealthyforSensitiveGroup,RDFS.subClassOf,NS.AQCategory))
g.add((NS.Unhealthy,RDF.type,OWL.Class))
g.add((NS.Unhealthy,RDFS.subClassOf,NS.AQCategory))
g.add((NS.VeryUnhealthy,RDF.type,OWL.Class))
g.add((NS.VeryUnhealthy,RDFS.subClassOf,NS.AQCategory))
g.add((NS.Hazardous,RDF.type,OWL.Class))
g.add((NS.Hazardous,RDFS.subClassOf,NS.AQCategory))

#Assigning Minimum and Maximum Values to AQ Categories
g.add((NS.Good,NS.hasminValue,Literal('0')))
g.add((NS.Good,NS.hasmaxValue,Literal('15')))
g.add((NS.Moderate,NS.hasminValue,Literal('15')))
g.add((NS.Moderate,NS.hasmaxValue,Literal('40')))
g.add((NS.UnhealthyforSensitiveGroup,NS.hasminValue,Literal('40')))
g.add((NS.UnhealthyforSensitiveGroup,NS.hasmaxValue,Literal('65')))
g.add((NS.Unhealthy,NS.hasminValue,Literal('65')))
g.add((NS.Unhealthy,NS.hasmaxValue,Literal('150')))
g.add((NS.VeryUnhealthy,NS.hasminValue,Literal('150')))
g.add((NS.VeryUnhealthy,NS.hasmaxValue,Literal('250')))
g.add((NS.Hazardous,NS.hasminValue,Literal('250')))
g.add((NS.Hazardous,NS.hasmaxValue,Literal('500')))



#Define Policy Type to Neighborhood
g.add((NS.hasPolicy, RDF.type, OWL.ObjectProperty))
g.add((NS.hasPolicy, RDFS.domain, NS.Neighborhood))
g.add((NS.hasPolicy, RDFS.range, NS.PolicyArea)) 

#Assign Air Quality Values
# g.add((NS.QualityIndex, RDF.type, NS.AQI))
# g.add((NS.QualityIndex, RDFS.label, Literal("Air Quality Index")))
# g.add((NS.QualityIndex, RDFS.comment, Literal("AQI values for different pollutants count")))


#Declare County Instance
county_uri=NS.LACounty
g.add((county_uri, RDF.type, NS.County))
g.add((county_uri, RDFS.label, Literal("LA")))


# Iterate over the rows in the DataFrame and create RDF triples for each Row

for i, row in df.iterrows():
        policy_uri=URIRef(f"{NS}Policy{row['Policy Area_x']}")
        g.add((policy_uri, RDF.type, NS.PolicyArea))
        g.add((policy_uri, RDFS.label, Literal(row['Policy Area_x'])))
        policy_uri2=URIRef(f"{NS}Policy{row['Policy Area_y']}")
        g.add((policy_uri2, RDF.type, NS.PolicyArea))
        g.add((policy_uri2, RDFS.label, Literal(row['Policy Area_y'])))
        condition_uri=URIRef(f"{NS}HealthCondition{row['Dataset_y']}")
        g.add((condition_uri, RDF.type, NS.HealthAffect))
        g.add((condition_uri, RDFS.label, Literal(row['Dataset_y'])))
        neighborhood_name=row['Neighborhood_x'].replace(" ","")
        neighborhood_uri=URIRef(f"{NS}{neighborhood_name}Neighborhood")
        g.add((neighborhood_uri, RDF.type, NS.Neighborhood))
        g.add((neighborhood_uri, RDFS.label, Literal(row['Neighborhood_x'])))
        g.add((neighborhood_uri, NS.isPartof, NS.LACounty))
        g.add((neighborhood_uri, NS.hasTract, URIRef(f"{NS}tract{row['Tract Number']}")))
        g.add((neighborhood_uri, NS.hasPolicy, URIRef(f"{NS}{row['Policy Area_x']}Policy")))
        g.add((neighborhood_uri, NS.hasPolicy, URIRef(f"{NS}{row['Policy Area_y']}Policy")))
        tract_uri=URIRef(f"{NS}tract{row['Tract Number']}")
        g.add((tract_uri, RDF.type, NS.Tract))
        g.add((tract_uri, RDFS.label, Literal(row['Tract Number'],datatype=XSD.integer)))
        g.add((tract_uri, NS.hasName, Literal(row['Tract_x'],datatype=XSD.string)))
        g.add((tract_uri, NS.hasGeoID, Literal(row['GEOID_x'],datatype=XSD.string)))
        location = row['Location_x']
        latitude, longitude = location.split(", ")
        g.add((tract_uri, NS.hasLatitude, Literal(latitude.strip("("),datatype=XSD.float)))
        g.add((tract_uri, NS.hasLongitude, Literal(longitude.strip(")"),datatype=XSD.float)))
        pollutant_name=row['Variable_x'].replace(" ","")
        pollutant_uri=URIRef(f"{NS}{pollutant_name}Pollutant")
        g.add((pollutant_uri, RDF.type, NS.Pollutant))
        g.add((pollutant_uri, RDFS.label, Literal(row['Variable_x'])))
        g.add((pollutant_uri, NS.affects, URIRef(f"{NS}{neighborhood_name}Neighborhood")))
        g.add((pollutant_uri, NS.hasHealthAffect, URIRef(f"{NS}HealthCondition{row['Dataset_y']}")))
        observation_uri=URIRef(f"{NS}HealthOutcome{i}")
        g.add((observation_uri, RDF.type, NS.HealthOutcome))
        g.add((observation_uri, RDFS.label, Literal(f"ER Visit Count with AQI value({row['Count_x']}) is {row['Count_y']} on {row['Date']} in {row['Tract_x']}")))
        g.add((observation_uri, NS.hasDate, Literal(row['Date'], datatype=XSD.dateTime)))
        g.add((observation_uri, NS.hasAQI, Literal(row['Count_x'],datatype=XSD.float)))
        g.add((observation_uri, NS.hasERVisit, Literal(row['Count_y'],datatype=XSD.float)))
        g.add((observation_uri, NS.ofTract, URIRef(f"{NS}tract{row['Tract Number']}")))

# Serialize the RDF graph to a file in XML format
g.serialize(destination='HealthOntology.rdf', format='xml')


