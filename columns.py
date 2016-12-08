fout=open("columns.txt","w+")
# first file:

with open('1-perform.csv', 'r') as f:
    line = f.readline()
# now the rest:
sel ="SELECT systemID,"
cols ="CREATE TABLE hp ( \n"
for words in line.split(','):
    word = words.rstrip('\n')
    if "Pct" in word or "MBPS" in word or 'Avg' in word:
        cols +="    " + word + ' numeric ,'+'\n'
        sel += " min(" + word + ") "+ "AS MIN"+word+ ", max(" + word + ") "+ "AS MAX"+word+ ", stddev(" +word + ") "+ "AS STDDEV"+word+ ", avg(" + word + ") "+ "AS AVG"+word+ ","
    elif 'from' in word or 'to'== word:
        cols +="    " + '"'+word+'"' + ' timestamp ,'+'\n'
    elif "UpSince" in word:
        cols +="    " + word + ' timestamp ,'+'\n'
    elif 'system' in word:
        cols +="    " + word + ' integer ,'+'\n'
    elif 'tpdKernel' in word:
        cols +="    " + word + ' varchar(50) ,'+'\n'
    elif 'TiBPr' in word:
        cols +="    " + word + ' numeric'+'\n'
        sel += " min(" + word + ") "+ "AS MIN"+word+ ", max(" + word + ") "+ "AS MAX"+word+ ", stddev(" +word + ") "+ "AS STDDEV"+word+ ", avg(" + word + ") "+ "AS AVG"+word+ ","
    else:
        cols +="    " + word + ' numeric ,'+'\n'
        sel += " min(" + word + ") "+ "AS MIN"+word+ ", max(" + word + ") "+ "AS MAX"+word+ ", stddev(" +word + ") "+ "AS STDDEV"+word+ ", avg(" + word + ") "+ "AS AVG"+word+ ","

cols += ');\n'
sel = sel[:-1]
cols += sel
print cols
fout.write(cols)
fout.close()
"""
\copy hp(systemId,"from","to",tpdKernelPatch,tpdKernelPatchPrevious,vvCountHistVlun,vvCountHistVlunPrevious,totalWriteIOsHistVlun,totalWriteIOsHistPortTargets,delAcks,delAcksPct,writesGt16s,writesGt32msPct,writesGt64msPct,writesGt128msPct,writesGt256msPct,writesGt512msPct,writesGt1024msPct,writesGt2048msPct,writesGt4096msPct,writes0_062msPct,writes0_125msPct,writes0_25msPct,writes0_5msPct,writes1msPct,writes2msPct,writes4msPct,writes8msPct,writes16msPct,writes32msPct,writes64msPct,writes128msPct,writes256msPct,writes512msPct,writes1024msPct,writes2048msPct,writes4096msPct,writes8192msPct,writes16384msPct,writes32768msPct,writes65536msPct,readsGt32msPct,readsGt64msPct,readsGt128msPct,readsGt256msPct,readsGt512msPct,readsGt1024msPct,readsGt2048msPct,readsGt4096msPct,reads0_062msPct,reads0_125msPct,reads0_25msPct,reads0_5msPct,reads1msPct,reads2msPct,reads4msPct,reads8msPct,reads16msPct,reads32msPct,reads64msPct,reads128msPct,reads256msPct,reads512msPct,reads1024msPct,reads2048msPct,reads4096msPct,reads8192msPct,reads16384msPct,reads32768msPct,reads65536msPct,totalsGt32msPct,totalsGt64msPct,totalsGt128msPct,totalsGt256msPct,totalsGt512msPct,totalsGt1024msPct,totalsGt2048msPct,totalsGt4096msPct,totals0_062msPct,totals0_125msPct,totals0_25msPct,totals0_5msPct,totals1msPct,totals2msPct,totals4msPct,totals8msPct,totals16msPct,totals32msPct,totals64msPct,totals128msPct,totals256msPct,totals512msPct,totals1024msPct,totals2048msPct,totals4096msPct,totals8192msPct,totals16384msPct,totals32768msPct,totals65536msPct,portReadBandwidthMBPS,portWriteBandwidthMBPS,portTotalBandwidthMBPS,cpuLatestSysAvgPct,cpuLatestUserAvgPct,cpuLatestTotalAvgPct,cpuLatestSysMaxPct,cpuLatestUserMaxPct,cpuLatestTotalMaxPct,portReadAvgIOSizeKB,portWriteAvgIOSizeKB,portTotalAvgIOSizeKB,ddsSizeUsedTiB,nodeUpSinceMostRecent,nodeCountOffline,nodeCountMissing,ddsSizeUsedTiBPrevious)
from '/Users/Nick_P/Documents/CS320/perform-csv/out.csv' DELIMITER ',' CSV HEADER

psql -h cs320ngg.cyxkzezznjnl.us-east-1.rds.amazonaws.com -U nperello -d HP_Systems -p 5432

\copy hp from '/Users/Nick_P/Documents/CS320/perform-csv/out.csv' DELIMITER ',' CSV HEADER
"""
