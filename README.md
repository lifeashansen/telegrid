## TELEGRID

Telegrid is a script that dumps chat ids for all entities in your telegram account:

&emsp; ie: Groups you are part of, channels you are subscribed to and users you have open conversations with

### How to use

- First, visit [`https://my.telegram.org/`](https://my.telegram.org/apps) and create an application to obtain the required `api_id` and `api_hash`

- Clone this repo

  ```
  git clone https://github.com/lifeashansen/telegrid.git && cd telegrid
  ```

- Sync all dependencies

  ```
  uv sync
  ```

- Telegrid expects `TELEGRAM_API_ID` and `TELEGRAM_API_HASH` variables to be set. This gets tiresome quickly, you can have a .env file and use [direnv](https://github.com/direnv/direnv.git) instead

  ```
  export TELEGRAM_API_ID="your_api_id_here" && export TELEGRAM_API_HASH="your_api_hash_here"
  ```

- Run the script

  ```
  uv run src/main.py
  ```

- You will be prompted to enter the phone number associated with your telegram account, then an otp for authorization and optionally a password if you have one set on your account

- Telegrid will write its output to these paths:
  - Channels: `${workDir}/output/channels.yaml`
  - Chats: `${workDir}/output/chats.yaml`
  - Users: `${workDir}/output/users.yaml`
