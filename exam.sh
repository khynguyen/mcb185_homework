gunzip -c ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz | grep -v "^#" | cut -f 7 | sort | uniq -c

gunzip -c ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz | cut -f9 | grep -c "transporter"
gunzip -c ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz | cut -f9 | grep -c "reductase"  