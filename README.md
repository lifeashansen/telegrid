## TELEGRID

Telegrid is a script that dumps chat ids for all entities in your telegram account
ie: Groups you are part of, channels you are subscribed to and users you have open conversations with

### How to use

- Clone this repo

  ```
  git clone https://github.com/lifeashansen/telegrid.git && cd telegrid
  ```

- Sync all dependencies

  ```
  uv sync
  ```

- Run the script

  ```
  uv run src/main.py
  ```

- You will be prompted to enter the phone number associated with your telegram account, then an otp for authorization and optionally a password if you have one set on your account

- Telegrid will write its output to these paths:
  - Channels: `${projectdir}/output/channels.yaml`
  - Chats: `${projectdir}/output/chats.yaml`
  - Users: `${projectdir}/output/users.yaml`
