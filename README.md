# Game Experiences Made in Sheffield

Welcome to the `gemsheffield.com` codebase! This repository is a simple static site which runs the website.

`gemsheffield.com` is a [Jekyll](https://jekyllrb.com/) site which is compiled to a static asset whenever the `main` branch is updated.

The website is currently hosted on [DigitalOcean](https://www.digitalocean.com/) (which is what `./do` is all about),
as a free static site. Whenever the `main` branch is updated, the site is rebuilt and redeployed.

## Running the app locally

1. [Install the prerequisites for Jekyll](https://jekyllrb.com/docs/installation/)
2. Run `bundle install`
3. Run `bundle exec jekyll serve`

This will host a hot-reloading version of the website on http://localhost:4000.

**Note**: the version of the website hosted live _isn't_ a live server, instead it builds the website to static HTML
files. This limits some of the nicer features of the app - for instance, we can't remove `.html` from all URLs unless
we change hosting methods.
