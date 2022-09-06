from sqlalchemy import Column, String, Boolean, DateTime


class BaseTemplateSQLModel:
    id = Column(
        String(63),
        primary_key=True,
        index=True,
    )
    create_date_time = Column(
        DateTime,
    )
    hashed = Column(
        String(511),
        index=True,
    )
    is_active = Column(
        Boolean,
        index=True,
        default=True,
    )

