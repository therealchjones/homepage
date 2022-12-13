#!/bin/sh

directory=`/bin/pwd` # which doesn't contain a trailing slash, except for /
category="${directory##*/}"
category=`echo "$category" | sed -r 's/^(.)(.*)/\U\1\E\2/'`

cat<<-EOF
Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>

<link type="text/css" href="../stylesheet.css" rel="stylesheet"
title="Default" />

<meta http-equiv="Content-type" content="text/html; charset=UTF-8" />

<title>Three-line Reviews: $category</title>

</head>

<body>

<h1><a href="http://www.aleph0.com/~chjones/threelinereviews/">Three-line
Reviews</a>: $category</h1>
EOF

if [ `ls -F | sed '/\/$/d' | wc -l` -eq 1 ]; then
	echo '<p id="noneavailable">No reviews are available at this time.</p>'
else
	echo '<dl id="reviewlist">'
	for file in *; do 
		if [ ! -d "$file" -a "$file" != "index.cgi" ]; then
			author="${file%% - *}"
			title="${file#* - }"
			echo -n '<dt>'
			if [ "$author" != "$title" ]; then
				echo -n "$author, "
			fi
			echo "<span class="longtitle">$title</span></dt><dd>"
			sed -n -r -e '${H;x;s/[\n\t ]+/ /g;s/^ //;s/ $//}' \
				-e '$s/ _([^_]+)_/ <span class="longtitle">\1<\/span>/g' \
				-e '$s/ \/([^\/]+)\// <em>\1<\/em>/g' \
				-e '$s/ \*([^\*]+)\*/ <strong>\1<\/strong>/g' \
				-e '$s/([^ ])'"'"'([^ ])/\1\&#39;\2/g' \
				-e '$s/"([^"]*)"/\&ldquo;\1\&rdquo;/g' \
				-e '${p;Q;}' \
				-e 'H' "$file"
			echo '</dd>'
		fi
	done
	echo '</dl><!-- reviewlist -->'
fi

cat<<-"EOF"
<div id="copyright">

<h2><a href="http://www.norightsreserved.org/"><img 
src="http://www.norightsreserved.org/img/NoRightsReserved-tiny.png"
alt="No Rights Reserved" /></a></h2>

<p>All information on this website (<a 
href="http://www.aleph0.com/">http://www.aleph0.com/</a>), unless
otherwise noted, is wholly the work of <a
href="http://www.aleph0.com/~chjones/">Christian&nbsp;Jones</a> (<a
href="mailto:chjones@aleph0.com">chjones@aleph0.com</a>).  All 
information, data, and formatting is hereby released into the public
domain, with no rights reserved.  For questions, concerns, or comments,
please <a href="mailto:chjones@aleph0.com">email the author</a>.</p>

</div><!-- copyright -->

</body>

</html>
EOF
