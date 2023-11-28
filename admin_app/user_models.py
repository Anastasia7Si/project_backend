import bcrypt
from sqlalchemy import Boolean, Integer, String, select, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from fastadmin import SqlAlchemyModelAdmin, register

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:dkflnfhfcjd2001@postgresql_db:5432/db_dealer'

sqlalchemy_engine = create_engine(
    'SQLALCHEMY_DATABASE_URL',
    echo=True,
)
sqlalchemy_sessionmaker = sessionmaker(sqlalchemy_engine,
                                       expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True,
                                    nullable=False)
    username: Mapped[str] = mapped_column(String(length=255),
                                          nullable=False)
    hash_password: Mapped[str] = mapped_column(String(length=255),
                                               nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False,
                                               nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False,
                                            nullable=False)

    def __str__(self):
        return self.username


@register(User, sqlalchemy_sessionmaker=sqlalchemy_sessionmaker)
class UserAdmin(SqlAlchemyModelAdmin):
    exclude = ("hash_password",)
    list_display = ("id", "username", "is_superuser", "is_active")
    list_display_links = ("id", "username")
    list_filter = ("id", "username", "is_superuser", "is_active")
    search_fields = ("username",)

    def authenticate(self, username, password):
        sessionmaker = self.get_sessionmaker()
        with sessionmaker() as session:
            query = select(User).filter_by(username=username,
                                           password=password,
                                           is_superuser=True)
            result = session.scalars(query)
            user = result.first()
            if not user:
                return None
            if not bcrypt.checkpw(password.encode(),
                                  user.hash_password.encode()):
                return None
            return user.id
