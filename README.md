This program is used to screen a VCF file to get only the variants that has no other variant in the vicinity. By default the programs selects the variants that has no other variant within 50bp on either side, however distance can be adjusted by passing `-d` argument. 

* The input VCF file must be sorted by the coordinates for this program to work


USAGE:

vcf_filter-adjacent.py -h -v <vcf-file> -d <distance>

    -h/--help: This usage help
    -v/--vcf-file: coordinate-sorted vcf
    -d/--distance: distance from the target SNP to remove adjacent variants [default 50]
    



Running the example files:
The example-data folder contains an input file, and an output file produced by following command

./vcf-adjecent-filter.py -v example-data/sample_input.vcf  -d 100 > example-data/sample_output_adj-100.vcf
