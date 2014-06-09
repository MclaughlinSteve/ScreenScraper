#! /usr/bin/perl -w

# Scrape1.cgi - demonstrate screen-scraping in Perl
# Steve McLaughlin

use strict;
use CGI;
use WWW::Mechanize;     # This is the object that gets stuff
use HTML::TokeParser;   # This is the object that parses HTML

# create new web agent and get a page
my $agent = WWW::Mechanize->new();

my $stream = HTML::TokeParser->new(\$agent->{content});


my $cgi = new CGI;

print $cgi->header(-type=>'text/html'),
      $cgi->start_html(-title=>'Web Comic Screen Scrape',
                        -author=>'Steve McLaughlin',
                        -style=>{'src'=>'/~mclaug67/style.css'});



# Go Ye Dogs scrape
$agent->get("http://www.goyedogs.com/");
$stream = HTML::TokeParser->new(\$agent->{content});

# Advance to the "div" tag we want:
my $tag = $stream->get_tag("div");

while($tag->[1]{id} and $tag->[1]{id} ne 'comic') {
	$tag = $stream->get_tag("div");
}

# Advance to the image:
my $toon = $stream->get_tag("img");

# get the attribute from the tag:
my $source = $toon->[1]{src};

# add this to the CGI output
print $cgi->h2('<a href = "http://www.goyedogs.com/">Go Ye Dogs</a>');
print $cgi->img({src=> $source, alt=>'Go Ye Dogs'}), "\n\n";



# Achewood comic scrape
$agent->get("http://www.moonbeard.com/");
$stream = HTML::TokeParser->new(\$agent->{content});

# Advance to the tag we want:
$tag = $stream->get_tag("div");

while($tag->[1]{id} and $tag->[1]{id} ne 'comic-1') {
	$tag = $stream->get_tag("div");
}

# Advance to the image:
$toon = $stream->get_tag("img");

# get the attribute from the tag:
$source = $toon->[1]{src};
#$source = 'www.achewood.com'.$source;

# Add this to the CGI output
print $cgi->h2('<a href = "http://www.moonbeard.com/">Moonbeard</a>');
print $cgi->img({src=> $source, alt=>'Moonbeard'}), "\n\n";





# Nedroid comic scrape
$agent->get("http://www.nedroid.com/");
$stream = HTML::TokeParser->new(\$agent->{content});

# Advance to the "div" tag we want:
$tag = $stream->get_tag("div");

while($tag->[1]{id} and $tag->[1]{id} ne 'comic') {
	$tag = $stream->get_tag("div");
}

# Advance to the image:
$toon = $stream->get_tag("img");

# get the attribute from the tag:
$source = $toon->[1]{src};

# add this to the CGI output
print $cgi->h2('<a href = "http://www.nedroid.com/">Nedroid</a>');
print $cgi->img({src=> $source, alt=>'Nedroid'}), "\n\n";





# The noob comic scrape
$agent->get("http://www.thenoobcomic.com/");
$stream = HTML::TokeParser->new(\$agent->{content});

# Advance to the "div"  tag we want:
$tag = $stream->get_tag("div");

while($tag->[1]{id} and $tag->[1]{id} ne 'main_content_comic') {
	$tag = $stream->get_tag("div");
}

# advance to the image:
$toon = $stream->get_tag("img");

# get the attribute from the tag:
$source = $toon->[1]{src};
$source = 'http://www.thenoobcomic.com/'. $source;

# add this to the CGI output
print $cgi->h2('<a href = "http://www.thenoobcomic.com/">The Noob Comic</a>');
print $cgi->img({src=> $source, alt=>'The Noob Comic'}), "\n\n";




#Saturday Morning Breakfast Cartoon Scrape
$agent->get("http://www.smbc-comics.com/");
$stream = HTML::TokeParser->new(\$agent->{content});

#Advance to the "div" tag we want:
$tag = $stream->get_tag("div");

while($tag->[1]{id} and $tag->[1]{id} ne 'comicimage'){
	$tag = $stream->get_tag("div");
}

# advance to the image:
$toon = $stream->get_tag("img");

# get the attribute from the tag:
$source = $toon->[1]{src};

#add this to the CGI output
print $cgi->h2('<a href = "http://www.smbc-comics.com/">Saturday Morning Breakfast Cereal</a>');
print $cgi->img({src=>$source, alt=>'Saturday Morning Breakfast Cereal'}), "\n\n";

# ALL DONE!
print $cgi->hr();
print $cgi->p('
    <a href ="http://validator.w3.org/check/referer">
        <img style="border:0;width:88px:height:31px"
            src="http://www.w3.org/Icons/valid-xhtml11"
            alt="Valid XHTML 1.1!">
    </a>

    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
');

print $cgi->end_html, "\n";
