# Project Title
**A short description of what the project is supposed to do & the most important facts to it.**  
<br/>
Project with T. Müller with the goal to spot craftsmen that may defrauding the company

## Project Description
**A detailed description of what the project is supposed to do & general details to it.**  
<br/>
Identify suspicous craftsmen that may be stealing materials or defrauding the company, by using the available data to the craftsmen *('completed-jobs', 'purchase-history' & 'van-inventory')* - this repo focuses on the year 2002. General details to the project, as well as details to the various approaches can be found in 'Docs/Presentation'.

## Data
**What data is available? What does it look like and where is is stored?!**  
<br/>

##### Bills
- Track the bought articles of a craftsman   
- Consits of all kind of bills *(not only material-bills...)*  
- Material-bills contain details like article-name, price, date of purchase, ...  
- Expert for this data M. Neuer & L. Sane  

##### Inventory
- Track the available articles at the beginning & end of a year *(inventory happens once a year)*  
- Article details like price, quantity, ... as well as craftsman- & van-ID    
- Expert for this data at B&O: M. Ligt  

## Code
**Description of the various scripts in this repository as well as the corresponding enviroments.**
<br/>

##### 01_inspect_raw_billing_data.Rmd
- Inspect 'Bills' data & collect questions/ things that are unclear  
- Renders a html-file with corresponding information to discuss it w/ M. Neuer & L. Sane    

##### 02_send_bill_SAP.py *('SAP' enviroment)*
- Detect suspicous bills & send them to SAP, so we can merge it into our data warehouse then 

## Folder-Structure
**What is the structure of the repository and where are the files at**  <br/>
```
├── README.md <- Top-level README for devs working with this repository
│ 
├── Data <- All the data for this repository
│   │   
│   ├─── raw <- Raw data of the repository
│   │     │
│   │     ├── Bills.csv: Data to the craftsmen bought articles  
│   │     └── Inventory.xlsx: Inventory of the craftsmen's vans
│   │
│   └─── processed <- Processed data of the repository
│         │ 
│         └── Bills_sus.json: Suspicous bills that need to be checked manually 
│  
├── Docs <- Sources, Results and everything else documenting the repository  
│   │  
│   ├─── Presentations <- Folder with all presentations 
│   ├─── Notes.txt: Personal notes to the projects with To-Do's, ...  
│   └─── Sources.txt: All relevant sources of the repository  
│
└── Code <- Code of the repository
    │
    ├── Example <- Templates, Examples & scripts to reproduce bugs
    ├── 01_inspect_raw_billing_data.Rmd 
    └── 02_send_bill_SAP.py
```

## Enviroments
**Description to the availabe enviroments of this repository**  
<br/>

Run PY-Scripts from the correct Conda-Environments!   
Install and activate a needed environment via `conda env create -f .\envs\`

###### spacy_transformers_WINDOWS.yml
Environment for everything on Windows OS (without GPU)

##### spacy_gpu_LINUX.yml
Environment for everything on Linux - especially finetuning of the model with GPU  