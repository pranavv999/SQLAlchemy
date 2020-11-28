# Dataproject-SQLAlchemy

## Analytics on UN Population

### Aim

1. To Transform the Population data from .csv file to **Postgresql database.**
2. Convert raw open data, country and year wise population estimates in this case, into charts that tell some kind of story.

### raw data

To get the raw Data in .csv file click [here.](https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv)

### How to run

There are two ways to run the program and they are mentioned below.

1. Through **Shell Script**.

    ```shell
    chmod a+rx script.sh
    ./script.sh
    ```

    Open __http://localhost:8000__ or [click here.](http://localhost:8000)

    Cleanup your Database by

    ```shell
    psql < destroy.sql
    ```

2. Run following commands in shell to see results.

    ```shell
    psql < create.sql
    ```

    ```shell
    python3 schema.py
    ```

    ```shell
    python3 main.py
    ```

    ```shell
    python3 json_generator.py
    ```

    Open __http://localhost:8000__ or [click here.](http://localhost:8000)

    Cleanup your Database by

    ```shell
    psql < destroy.sql
    ```