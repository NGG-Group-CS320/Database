# Database 
Tutorials
* http://sqlitebrowser.org its SQLite but you can insert small databases to practice basic SQL  
* Here is a file you can practice with: 
https://drive.google.com/file/d/0ByIak094YnTPMm9RbXB2ckhNWGc/view?usp=sharing 
* Also basic python tutorial that I personally used to begin learning it: s
Python 3: https://learnxinyminutes.com/docs/python3/ 

Old Info you gotta know to connect
* Host: cs320ngg.cyxkzezznjnl.us-east-1.rds.amazonaws.com
* Database: HP_Systems
* User: backend
* Password: PM me for this
* psql -h cs320ngg.cyxkzezznjnl.us-east-1.rds.amazonaws.com -U backend -d HP_Systems -p 5432

NEW INFO TO CONNECT
* Host: ssh.mfdat.host
* Database: HP_Project
* User: backend
* Password: PM me for this
* psql -h ssh.mfdat.host -U backend -d HP_Project -p 5432

Tables/Views
* hp: the old table before column adding and computations
* hp_stats: contains min, max, avg, and stdDev for each system
* hpnmb: the new all system hp table, has added computaions and columns
* health_scores: table containing the different scores calculated in python
* health_scores_scala: table containing the different scores calculated in scala
* normalized_bandwith_date: contains misspelling but the rest of the queries use it 
 computes normalized bandwidth for systems (bandwidth/maxBandwidth)

Many of the queries used can be found in querydump.sql
