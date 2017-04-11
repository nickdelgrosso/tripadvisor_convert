# tripadvisor_convert

A Python script for converting JSON files from a dataset containing TripAdvisor Reviews to Pandas DataFrames or CSV Files, for simpler processing.

http://sifaka.cs.uiuc.edu/~wang296/Data/index.html

## Installation

Clone this repo and install from the command line:

    python setup.py install traipadvisor_convert

or using pip:

    pip install git+git://github.com/neuroneuro15/tripadvisor_convert


## Usage

    import tripadvisor_convert
    
    json_file = 'examples/73739.json'
    df = tripadvisor_convert.to_df(json_file)
    print(df.head(5))
