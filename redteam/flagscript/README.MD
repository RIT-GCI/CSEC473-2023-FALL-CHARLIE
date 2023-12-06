# Let's make some fake flags

Running this app is easy, just run `python3 flag_gen.py`.
It will ask you some questions, then generate the flags.

To configure it, edit the fields in `flag_conf.py`.

## What it will ask
* For generating directories, use:
    * 1: dirs
        * This option will choose random directories from 
          `dirs` in `flag_conf.py`
    * 2: random
        * This option will choose a random directory
        * If you choose this option, it will ask for a max depth.
        That's how many sub folders from `/` it will traverse.
* For generating filenames, use:
    * 1: fnames
        * This option will choose random names from `fnames`
        in `flag_conf.py`
    * 2: alpha
        * This option will generate random names using the alphabet
    * 3: alpha_num
        * This option will generate random names using the alphabet and numbers
    * 4: random
        * This option will generate random names using any ascii characters
    * If you choose any option other than fnames you will prompted to
    provide a length for the file names
* Number to generate:
    * This is how many fake flags to generate

## Configurable fields
`flag_conf.py` has some info in it you can change:
* `dirs`
    * This is a list of directories to choose from if you decide
    to use the `dirs` option
* `fnames`
    * This is a list of file names to choose from if you decide
    to use the `fnames` option
* `alpha`
    * This should contain the alphabetic characters, doesn't need changing
* `alpha_num`
    * This should contain the alphanumeric characters, doesn't need changing
* `all_chrs`
    * This should contain all the ascii characters, doesn't need changing
* `fake_prefixes`
    * This is a list of fake prefixes, that is to say what is put firs in the
    flag format. See the note from gray team for what is illegal to include.
* `fake_flags`
    * This is a list of fake flags, that is to say what is actually put inside 
    the brackets of the flag format. According to gray team, must specify that
      it's fake.