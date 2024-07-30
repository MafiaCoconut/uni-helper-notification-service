from datetime import datetime, UTC
from typing import Annotated
from sqlalchemy.orm import mapped_column
from sqlalchemy import text

intpk = Annotated[int, mapped_column(primary_key=True)]

created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=lambda: datetime.now(UTC).replace(tzinfo=None),
)]
