# lib

To enable prompt collapsing in agnoster, replace the `prompt_dir()` with 

```sh
prompt_dir() {
  prompt_segment blue black $(pwd | perl -pe "
     BEGIN {
         binmode STDIN,  ':encoding(UTF-8)';
         binmode STDOUT, ':encoding(UTF-8)';
     }; s|^$HOME|~|g; s|/([^/])[^/]*(?=/)|/\$1|g
   ")
}
```