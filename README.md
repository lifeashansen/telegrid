## TELEGRID

- Telegrid is a script that dumps all chat ids in your telegram account

### How to use

Currently, `telegrid` is not available in pypi

- Clone this repo

  ```
    git clone https://github.com/lifeashansen/telegrid.git && cd telegrid

  ```

- Sync all dependencies

  ```

  ```

- Run the script

  ```
  uv run src/main.py
  ```

- You will be prompted to enter the phone number associated with your telegram account, then an otp for authorization and optionally a password if you have one set on your account

- Telegrid will dump output in
  - Channels: `${projectdir}/output/channels.yaml`
  - Chats: `${projectdir}/output/chats.yaml`
  - Users: `${projectdir}/output/users.yaml`
