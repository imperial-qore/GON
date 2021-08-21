from src.parser import *
from src.folderconstants import *

# Threshold parameters
lm_d = {
		'SMD': [(0.997, 1), (0.99995, 1.06), (0.99995, 1.06)],
		'synthetic': [(0.999, 1), (0.999, 1), (0.999, 1)],
		'FTSAD-1': [(0.993, 1), (0.993, 1), (0.9999, 1.01)],
		'FTSAD-25': [(0.98, 1), (0.98, 1), (0.98, 1)],
		'FTSAD-55': [(0.999, 1), (0.999, 1.04), (0.999, 1.04)],
		'WADI': [(0.99, 1), (0.999, 1), (0.999, 1)],
		'MSDS': [(0.91, 1), (0.9996, 1.04), (0.9, 1.04)],
	}
lm = lm_d[args.dataset][1 if 'TranAD' in args.model else 2 if 'SAN' in args.model else 0]

# Hyperparameters
lr_d = {
		'SMD': 0.0001, 
		'synthetic': 0.0001, 
		'FTSAD-1': 0.008, 
		'FTSAD-25': 0.001, 
		'FTSAD-55': 0.002, 
		'WADI': 0.0001, 
		'MSDS': 0.001, 
	}
lr = lr_d[args.dataset]

lr_SAN = {
		'SMD': 0.0001, 
		'synthetic': 0.0005, 
		'FTSAD-1': 0.0005, 
		'FTSAD-25': 0.0005, 
		'FTSAD-55': 0.0005, 
		'WADI': 0.0005, 
		'MSDS': 0.0005, 
	}
lrSAN = lr_SAN[args.dataset]


# Debugging

preds = []
debug = 9