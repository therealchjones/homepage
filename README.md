Christian Jones's personal homepage at https://aleph0.com/~chjones is managed
via a git repository housed on GitHub at
https://github.com/therealchjones/homepage. This includes both files (such as
`index.html` and `README.md`) that will be copied to the aleph 0 webserver when
appropriate as well as GitHub workflows for making such deployments
automatically.

If you're reading a copy of this README.md file on the aleph 0 (DreamHost)
webserver, please don't modify the files here; your changes may be overwritten,
you may mess up the GitHub workflows, or your changes may just never be saved
properly. The correct process to use is one which results in pushing desired
changes to the GitHub repository's main branch, after which the proper GitHub
workflow will take over.

Finally, please note that the current workflows do _not_ remove any files from
the aleph 0 webserver. The failure to remove files is
considered a safety feature rather than a bug. If files need to be removed, they
should first be removed from the git repository (and the changes should be
pushed), then removed from the webserver manually.
