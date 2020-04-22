# Invitation Generation 

This repo contains a set of Python/bash scripts that can be used to automatically generate Latex documents where only a few parameters like names, language (i.e., input file) used or certain flags change.  

## System requirements

The bash scripts `mk*` will work on Unix-based systems.  

You will need to install the [webomints font](https://ctan.org/pkg/webomints?lang=en) on your system in order for setting the decorations, correctly.

## File structure

The invitation is written in Latex, with the main text contained in language-specific files (`dt.tex`, `en.tex`, `zh.tex`). The overall document is `invitation.tex`, containing all elements that are identical over all languages (pictures, decorations, etc.).  

Within `settings.tex`, special bits can be specified, like for example the poem at the end of the document, or the pdf hyperparameters.  The `setPersonal.tex` file is used to generate the substitutes for each individual file, e.g., the guest's names or the language in which to typeset.  

All parameters can be set in the file `guests.csv`. Here, the first line can be used for remembering which column contains what information, the others describe one document per line.   

## Usage 

For typesetting a single document according to the parameters currently present in `setPersonal.tex`, use `./mk`. For batch processing according to `guests.csv`, use `python3 Process.py`. This will typeset one document per line in `guests.csv`, placing generated documents in the `output` folder, assigning a document name according to the name of the invitee.  
 

## Improvements

Potentially, instead of the Python script also [GNU parallel](https://gnu.org/software/parallel/man.html) can be used. The rest of the files should still be quite useful, I hope.   

### TODOs
- Add comments to scripts 
- Tidy up the python script

