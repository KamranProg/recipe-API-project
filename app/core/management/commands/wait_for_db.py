import time
import os
from psycopg2 import connect, OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Wait for database to become available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for Postgres...")

        retries = 10
        while retries:
            try:
                conn = connect(
                    dbname=os.environ["POSTGRES_DB"],
                    user=os.environ["POSTGRES_USER"],
                    password=os.environ["POSTGRES_PASSWORD"],
                    host=os.environ["POSTGRES_HOST"],
                    port=os.environ["POSTGRES_PORT"],
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS("Postgres is available"))
                return
            except OperationalError:
                retries -= 1
                self.stdout.write("Postgres unavailable, waiting 2s...")
                time.sleep(2)

        self.stderr.write(self.style.ERROR("DB still not available — exiting"))
        raise Exception("Postgres not available")
