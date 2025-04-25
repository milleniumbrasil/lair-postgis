# Examples

## Basic Example

 ```bash
 lair-postgis --in ./schema/lair.sql --out ./deploy
 ```

 This will create:

 ```text
 deploy/
 ├── Dockerfile
 ├── docker-compose.yml
 └── init-db/
     ├── 01-init.sql
     └── 10-lair.sql
 ```

## After Scaffold

 To run the database:

 ```bash
 cd deploy
 docker compose down -v && docker compose up --build -d
 ```