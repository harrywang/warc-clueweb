import warc
f = warc.open("./sample_data/ClueWeb09_English_Sample_File.warc.gz")
for record in f:
    print record.header.get('WARC-Target-URI'), record['Content-Length']
