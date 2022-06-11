Mapillary Proxy
---

This is a very simple cached proxy to Mapillary which helps you to get a thumbnail of your target image.

# Getting started

The following environment keys can be used to configure this project:

- `MAPILLARY_APP_TOKEN` - the client app token you can [get on this page](https://www.mapillary.com/dashboard/developers)

## Deployment

These can be added using Heroku's add project or Settings interface:

[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/streetwise/mapillary-proxy)

Or through the environment variables on Vercel:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/streetwise/mapillary-proxy)

## Tech stack

* [Falcon](https://falcon.readthedocs.io/) - a lightweight, superfast Python framework
* [Requests](https://pypi.org/project/requests/) - the one and only
* [Falcon-Caching](https://pypi.org/project/falcon-caching/) - speed me up

# Contributing

First, clone this repository and make sure to set up the following dependencies:

- [X] [Python 3](https://python.org)
- [X] [Poetry](https://python-poetry.org/docs/)
- [X] [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) or [Vercel CLI](https://vercel.com/download) (optional)

Setup a virtual environment, install dependencies, and activate it using Poetry:

```
$ poetry shell
$ poetry install
```

Create a file called `.flaskenv` (or `.env` if using gunicorn in production) in the root folder and add development settings and required keys from the Configuration section above.

Now start the development server:

```
$ gunicorn --reload index
```

- The API will be served from `localhost:8000/thumb?key=...`
- Using [httpie](https://httpie.io/) for testing is encouraged

# License

[MIT License](LICENSE.md)
