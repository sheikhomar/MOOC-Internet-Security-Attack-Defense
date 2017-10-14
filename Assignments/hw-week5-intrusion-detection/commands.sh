# Generate top 10 Src IP Addr ordered by flows to port 22
nfdump -R nfdump_ssh_analysis_04/ -s srcip/flows 'dst port 22'

# How many destination has TS contacted? Assume that TS is 210.89.244.204
nfdump -R nfdump_ssh_analysis_04/ -A dstip 'src ip 210.89.244.204'

# Top 10 dst IPs that generated the most bytes contacted by the TS
nfdump -R nfdump_ssh_analysis_04/ -s dstip/bytes 'src ip 210.89.244.204'

# What is the average PPF (calculated as #packets/#flows) for TS in the nfanon.201312080640 file?
# Use the summary to calculate the PPF
nfdump -r nfdump_ssh_analysis_04/nfanon.201312080640 'src ip 210.89.244.204' > ppf
