# haip.config

[![License](https://img.shields.io/github/license/haipdev/confluence.svg)](LICENSE)
[![Build Status](https://travis-ci.org/haipdev/confluence.svg?branch=master)](https://travis-ci.org/haipdev/confluence)

haip.confluence is a simple module to communicate with confluence REST API.

## Features

-   **getBody**: get confluence page by id
-   **setBody**: set confluence page content by id

## Getting Started

### Installing

```sh
pip install haip-confluence
```

or from source:

```sh
git clone https://github.com/haipdev/confluence.git
```

### Example

#### config-files

/path-to-my-config-dir/confluence.yml

```yaml
confluence:
    url: https://myconfluence.domain.com/rest/api/latest
    username: user
    password: pass
    timeout: 10
```

#### python implementation

```python
import haip.config as config
import haip.confluence as confluence

config.load('/path-to-my-config-dir', 'dev')
content = confluence.getContent(12345)
```

## Running the tests

Tests are written using pytest and located in the "tests" directory.

```sh
pytest tests
```

## Contributing

Feel free to use and enhance this project. Pull requests are welcome.

## Authors

-   **Reinhard Hainz** - _Initial work_ - [haipdev](https://github.com/haipdev)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Dependencies

-   [haip-config](https://github.com/haipdev/config)
