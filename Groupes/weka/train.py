#!/bin/env python3

import argparse
import xml.etree.ElementTree as ET
from getfeatures import features, getfeature
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier
import weka.core.serialization as serialization

aparser = argparse.ArgumentParser(description='Train model')
aparser.add_argument('input', help='Input file')
aparser.add_argument('model', help='Model file')
args = aparser.parse_args()

print('Reading corpus and writing features to arff')
arffile = open("train.arff", "w")
xmlcorpus = ET.parse(args.input)
docs = xmlcorpus.getroot().getchildren()
featurekeys = sorted(list(features.keys()))
arffile.write('@relation fakevstrusted\n')
for feature in featurekeys:
	arffile.write('@attribute '+feature+' numeric\n')
arffile.write('@attribute class {fake,trusted,parodic}\n')
arffile.write('@data\n')
for i in range(len(docs)):
	docfeatures = []
	for j in range(len(featurekeys)):
		doc = docs[i]
		featurename = featurekeys[j]
		docfeatures.append(str(getfeature(doc, featurename)))
	docfeatures.append(doc.get('class'))
	arffile.write(','.join(docfeatures)+'\n')
arffile.close()

print('Démarrage de la jvm et chargement des données dans weka')
jvm.start()
loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file("train.arff")
data.class_is_last()

print('Apprentissage du modèle')
classifier = Classifier(classname="weka.classifiers.bayes.NaiveBayesMultinomial")
classifier.build_classifier(data)

### Ici enregistrer le modèle dans le fichier dont le chemin est fourni par args.model
serialization.write(args.model, classifier)

print('Extinction de la jvm')
jvm.stop()