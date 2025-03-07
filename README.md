
# Running for develop

## Start database container

Start database using VSCode *tasks* ( see `.vscode/tasks.json`). The configured task will run the *db* service defined in `./docker-compose.yml`.

## Running the Back End

To create Virtualenv, activate and install requirements:

```bash
cd be
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To run the backend app:

```sh
fastapi dev main.py
```

or, alternatively, use the saved VSCode launch configuration ( see `.vscode/launch.json`)


## Running the Front End

```sh
cd fe
npm install
npm dev
```

Keep in mind that:

- `npm run dev` ( or `vite` ) starts a local web server with Hot Module Replacement for development, and will automatically change when code changes
- `npm run build` ( or `npm run dev` ) builds the project, and outputs to the folder ./dist
- `npm run preview` ( or `vite preview` ) start a local web server that serves the built solution from ./dist for previewing

