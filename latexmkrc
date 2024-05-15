# Use XeLaTeX by default
$latex = 'xelatex';

# Set the output directory for generated files
$out_dir = 'build';

# Ensure the directory exists
mkdir $out_dir unless -d $out_dir;

# Set the directory for auxiliary files
$aux_dir = 'build';

