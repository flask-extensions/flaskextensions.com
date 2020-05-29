![Codeshow](https://github.com/flask-extensions/flaskextensions.com/workflows/Codeshow/badge.svg)

# FlaskExtensions.com

<img src="./assets/diagram.png" height="400">


Website http://flaskextensions.com curated collection of Flask Extensions and its resources


<img src="./assets/screenshot.png" width="300">
<img src="./assets/fex_search_screenshot.png" width="300">


## Why?

There are some amazing Flask Extensions spread across github and gitlab repositories but we miss a place to aggregate and follow status of them all.

## How?

This project has been develped during live coding streams at https://twitch.tv/codeshow

## Stack

This project is divided in some services:

- **FEXService**

  Powered by **Python sched** Fetches data from Github API for every repo having `flask-extension` as a topic.

- **FEXAPI**

  Powered by **FastAPI** serves the data and provides search, pagination, aggregation etc.

- **FEXUI**

  Powered by **Vue.js** and **Bulma CSS** shows the web grid to search extensions.

- **FEXTUI** (__todo__)

  Powered by **Typer** and **Blessed** gives a UI to explore extensions at the terminal

- **FEXWASM** (__todo__)

  Powered by **Rust** and **WebAssembly** gives the same experience as desktop app

- **FEXAPP** (__todo__)

  **To Be Defined**


## Contributing

Read the instructions on [CONTRIBUTING.md](CONTRIBUTING.md)


## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://brunorocha.org"><img src="https://avatars2.githubusercontent.com/u/458654?v=4" width="100px;" alt=""/><br /><sub><b>Bruno Rocha</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=rochacbruno" title="Code">💻</a> <a href="#video-rochacbruno" title="Videos">📹</a> <a href="#ideas-rochacbruno" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-rochacbruno" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://mtrsk.gitlab.io/"><img src="https://avatars0.githubusercontent.com/u/16356569?v=4" width="100px;" alt=""/><br /><sub><b>Marcos Benevides</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=mtrsk" title="Code">💻</a> <a href="https://github.com/flask-extensions/flaskextensions.com/pulls?q=is%3Apr+reviewed-by%3Amtrsk" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=mtrsk" title="Tests">⚠️</a> <a href="#infra-mtrsk" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#maintenance-mtrsk" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://fabricio-aguiar.github.io/"><img src="https://avatars1.githubusercontent.com/u/17153022?v=4" width="100px;" alt=""/><br /><sub><b>Fabricio Aguiar</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/pulls?q=is%3Apr+reviewed-by%3Afabricio-aguiar" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=fabricio-aguiar" title="Code">💻</a></td>
    <td align="center"><a href="http://jairomr.com.br"><img src="https://avatars0.githubusercontent.com/u/7321240?v=4" width="100px;" alt=""/><br /><sub><b>Jairo Matos Da Rocha</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=jairomr" title="Code">💻</a> <a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=jairomr" title="Documentation">📖</a> <a href="https://github.com/flask-extensions/flaskextensions.com/pulls?q=is%3Apr+reviewed-by%3Ajairomr" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/ddauriol"><img src="https://avatars0.githubusercontent.com/u/44655942?v=4" width="100px;" alt=""/><br /><sub><b>Douglas Maciel d'Auriol Souza</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=ddauriol" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/marcosf63"><img src="https://avatars1.githubusercontent.com/u/4137898?v=4" width="100px;" alt=""/><br /><sub><b>Marcos Oliveira</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=marcosf63" title="Code">💻</a></td>
    <td align="center"><a href="http://youtube.com/c/eduardomendes"><img src="https://avatars1.githubusercontent.com/u/6801122?v=4" width="100px;" alt=""/><br /><sub><b>Eduardo Mendes</b></sub></a><br /><a href="#tutorial-dunossauro" title="Tutorials">✅</a> <a href="#video-dunossauro" title="Videos">📹</a> <a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=dunossauro" title="Code">💻</a> <a href="https://github.com/flask-extensions/flaskextensions.com/pulls?q=is%3Apr+reviewed-by%3Adunossauro" title="Reviewed Pull Requests">👀</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://blog.doseextra.com"><img src="https://avatars1.githubusercontent.com/u/15989303?v=4" width="100px;" alt=""/><br /><sub><b>Regis Tomkiel</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=rtomkiel" title="Code">💻</a> <a href="#example-rtomkiel" title="Examples">💡</a></td>
    <td align="center"><a href="http://spacedevs.com.br"><img src="https://avatars2.githubusercontent.com/u/9499562?v=4" width="100px;" alt=""/><br /><sub><b>Marcus Pereira</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=MarcusMann" title="Code">💻</a> <a href="#ideas-MarcusMann" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://devgiordane.com"><img src="https://avatars1.githubusercontent.com/u/7908354?v=4" width="100px;" alt=""/><br /><sub><b>Giordane Oliveira</b></sub></a><br /><a href="#design-devgiordane" title="Design">🎨</a> <a href="#ideas-devgiordane" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/herbety-paulo-aa9a2b186/"><img src="https://avatars0.githubusercontent.com/u/51804133?v=4" width="100px;" alt=""/><br /><sub><b>Herbety Paulo</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=Pbezerra-dev" title="Code">💻</a> <a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=Pbezerra-dev" title="Documentation">📖</a></td>
    <td align="center"><a href="http://www.vicentemarcal.unir.br"><img src="https://avatars2.githubusercontent.com/u/26264782?v=4" width="100px;" alt=""/><br /><sub><b>Vicente Marçal</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/pulls?q=is%3Apr+reviewed-by%3Ariverfount" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=riverfount" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/walison17"><img src="https://avatars3.githubusercontent.com/u/14242043?v=4" width="100px;" alt=""/><br /><sub><b>Walison Filipe</b></sub></a><br /><a href="#ideas-walison17" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://bergpb.github.io"><img src="https://avatars1.githubusercontent.com/u/11005963?v=4" width="100px;" alt=""/><br /><sub><b>Berg Paulo</b></sub></a><br /><a href="https://github.com/flask-extensions/flaskextensions.com/commits?author=bergpb" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
